from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import EffectInstanceDice
from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import WeaponWrapper
from com.ankamagames.dofus.internalDatacenter.spells.EffectZone import EffectZone
from com.ankamagames.dofus.internalDatacenter.stats.entityStats import EntityStats
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import CurrentPlayedFighterManager
from com.ankamagames.dofus.network.enums.CharacterSpellModificationTypeEnum import CharacterSpellModificationTypeEnum
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import EnterFrameDispatcher
from com.ankamagames.jerakine.utils.display.spellZone.ICellZoneProvider import ICellZoneProvider
from com.ankamagames.jerakine.utils.display.spellZone.IZoneShape import IZoneShape
from damageCalculation.tools.StatIds import StatIds


class SpellWrapper(Proxy, ISlotData, IClonable, ICellZoneProvider, IDataCenter):
   
   _cache:list = []
   
   _playersCache:dict = dict()
   
   _cac:'SpellWrapper'
   
   _errorIconUri:Uri
   
   logger = Logger(__name__)
   
   BASE_DAMAGE_EFFECT_IDS:list = [100,96,97,98,99,92,93,94,95,1012,1013,1014,1015,1016]
   
   _uri:Uri
   
   _slotDataHolderManager:SlotDataHolderManager
   
   _canTargetCasterOutOfZone:object
   
   _variantActivated:bool
   
   _spellLevel:SpellLevel
   
   _spell:Spell
   
   id:int = 0
   
   spellLevel:int = 1
   
   effects:list[EffectInstance]
   
   criticalEffect:list[EffectInstance]
   
   gfxId:int
   
   playerId:float
   
   versionNum:int
   
   additionalEffectsZones:list[EffectZone]
   
   _actualCooldown:int = 0
   
   def __init__(self):
      super().__init__()
   
   def getEntityId(self) -> float:
      if PlayedCharacterApi().isInFight():
         return CurrentPlayedFighterManager().currentFighterId
      return PlayedCharacterManager().id
   
   def create(self, spellID:int, spellLevel:int = 0, useCache:bool = True, playerId:float = 0, variantActivated:bool = False, areModifiers:bool = True) -> SpellWrapper:
      spell:SpellWrapper = None
      if spellID == 0:
         useCache = False
      if useCache:
         if self._cache[spellID] and not playerId:
            spell = self._cache[spellID]
         elif self._playersCache[playerId] and self._playersCache[playerId][spellID]:
            spell = self._playersCache[playerId][spellID]
      if spellID == 0 and _cac != None:
         spell = _cac
      if not spell:
         spell = SpellWrapper()
         spell.id = spellID
         if useCache:
            if playerId:
               if not self._playersCache[playerId]:
                  self._playersCache[playerId] = []
               if not self._playersCache[playerId][spellID]:
                  self._playersCache[playerId][spellID] = spell
            else:
               self._cache[spellID] = spell
         spell._slotDataHolderManager = SlotDataHolderManager(spell)
      if spellID != 0 or not _cac:
         if spellID == 0:
            _cac = spell
         spell.id = spellID
         spell.gfxId = spellID
         spell.variantActivated = variantActivated
      spell.playerId = playerId
      spellData:Spell = Spell.getSpellById(spellID)
      if not spellData:
         return None
      if spellLevel == 0:
         spell.updateSpellLevelAccordingToPlayerLevel()
      else:
         spell.spellLevel = spellLevel
         spell._spellLevel = spellData.getSpellLevel(spell.spellLevel)
      spell.setSpellEffects(areModifiers)
      return spell
   
   def getSpellWrapperById(self, spellId:int, playerID:float, forceCreate:bool = False) -> SpellWrapper:
      if forceCreate:
         return create(spellId)
      if playerID != 0:
         if not self._playersCache[playerID]:
            return None
         if not self._playersCache[playerID][spellId] and self._cache[spellId]:
            self._playersCache[playerID][spellId] = self._cache[spellId].clone()
         if spellId == 0:
            return _cac
         if self._playersCache[playerID][spellId]:
            return self._playersCache[playerID][spellId]
         return None
      return self._cache[spellId]
   
   def refreshAllPlayerSpellHolder(self, playerId:float) -> None:
      EnterFrameDispatcher().worker.addUniqueSingleTreatment(SpellWrapper, self.refreshSpellHolders,[playerId])
   
   def refreshSpellHolders(self, playerID:float) -> None:
      wrapper:SpellWrapper = None
      for wrapper in self._playersCache[playerID]:
         if wrapper:
            wrapper._slotDataHolderManager.refreshAll()
      if _cac:
         _cac._slotDataHolderManager.refreshAll()
   
   def resetAllCoolDown(self, playerId:float, accessKey:object) -> None:
      wrapper:SpellWrapper = None
      SecureCenter.checkAccessKey(accessKey)
      for wrapper in self._playersCache[playerId]:
         wrapper.actualCooldown = 0
   
   def removeAllSpellWrapperBut(self, playerId:float, accessKey:object) -> None:
      id = None
      num:int = 0
      i:int = 0
      SecureCenter.checkAccessKey(accessKey)
      temp:list = []
      for id in self._playersCache:
         if float(id) != playerId:
            temp.append(id)
      num = len(temp)
      i = 0
      while i < num:
         del self._playersCache[temp[i]]
         i += 1
   
   def removeAllSpellWrapper(self) -> None:
      self._playersCache = dict()
      self._cache = []

   @property
   def actualCooldown(self) -> int:
      return int(self._actualCooldown) if PlayedCharacterManager().isFighting else int(0)
   
   @actualCooldown.setter
   def actualCooldown(self, u:int) -> None:
      self._actualCooldown = u
      self._slotDataHolderManager.refreshAll()
   
   @property
   def spellLevelInfos(self) -> SpellLevel:
      return self._spellLevel
   
   def updateSpellLevelAndEffectsAccordingToPlayerLevel(self) -> None:
      self.updateSpellLevelAccordingToPlayerLevel()
      self.setSpellEffects()
   
   @property
   def variantActivated(self) -> bool:
      return self._variantActivated
   
   @variantActivated.setter
   def variantActivated(self, value:bool) -> None:
      self._variantActivated = value
   
   @property
   def minimalRange(self) -> int:
      return self["minRange"]
   
   @property
   def maximalRange(self) -> int:
      return self.spellLevelInfos.range
   
   @property
   def castZoneInLine(self) -> bool:
      return self["castInLine"]
   
   @property
   def castZoneInDiagonal(self) -> bool:
      return self["castInDiagonal"]
   
   @property
   def spellZoneEffects(self) -> list[IZoneShape]:
      if InventoryManager().currentBuildId != -1:
         for build in InventoryManager().builds:
            if build.id == InventoryManager().currentBuildId:
                   break
         if self.id == 0:
            for iw in build.equipment:
               if isinstance(iw, WeaponWrapper):
                  break
            if not isinstance(iw, WeaponWrapper) and self.spellLevelInfos:
               return self.spellLevelInfos.spellZoneEffects
      if self.id != 0 or not PlayedCharacterManager().currentWeapon:
         if self.spellLevelInfos:
            return self.spellLevelInfos.spellZoneEffects
      return None
   
   @property
   def hideEffects(self) -> bool:
      if self.id == 0 and PlayedCharacterManager().currentWeapon != None:
         return PlayedCharacterManager().currentWeapon.hideEffects
      if self.spellLevelInfos:
         return self.spellLevelInfos.hideEffects
      return False
   
   @property
   def info1(self) -> str:
      if self.actualCooldown == 0 or not PlayedCharacterManager().isFighting:
         return None
      if self.actualCooldown == 63:
         return "-"
      return str(self.actualCooldown)
   
   @property
   def startTime(self) -> int:
      return 0
   
   @property
   def endTime(self) -> int:
      return 0
   
   @endTime.setter
   def endTime(self, t:int) -> None:
          pass
   
   @property
   def timer(self) -> int:
      return 0
   
   @property
   def active(self) -> bool:
      if not PlayedCharacterManager().isFighting:
         return True
      return bool(CurrentPlayedFighterManager().canCastThisSpell(self.spellId,self.spellLevel))
   
   @property
   def spell(self) -> Spell:
      if not self._spell:
         self._spell = Spell.getSpellById(self.id)
      return self._spell
   
   @property
   def spellId(self) -> int:
      if self.spell:
         return self.spell.id
      return 0
   
   @property
   def playerCriticalRate(self) -> int:
      currentCriticalHitProbability:float = None
      weaponCriticalHit:int = 0
      entityId:float = None
      stats:EntityStats = None
      totalCriticalHit:float = None
      criticalRate:int = 0
      if self["isSpellWeapon"] and not self["isDefaultSpellWeapon"]:
         weaponCriticalHit = self.getWeaponProperty("criticalHitProbability")
         currentCriticalHitProbability = float(55 - weaponCriticalHit) if weaponCriticalHit > 0 else float(0)
      else:
         currentCriticalHitProbability = self.getCriticalHitProbability()
      spellModifier:SpellModifier = SpellModifiersManager().getSpellModifier(self.getEntityId(),self.id,CharacterSpellModificationTypeEnum.CRITICAL_HIT_BONUS)
      if spellModifier is not None:
         currentCriticalHitProbability = float(currentCriticalHitProbability - spellModifier.totalValue) if currentCriticalHitProbability > 0 else float(0)
      if currentCriticalHitProbability is not None:
         entityId = self.getEntityId()
         stats = None
         if entityId is not None:
            stats = StatsManager().getStats(entityId)
         if stats is not None:
            totalCriticalHit = stats.getStatTotalValue(StatIds.CRITICAL_HIT) - stats.getStatAdditionalValue(StatIds.CRITICAL_HIT)
            criticalRate = currentCriticalHitProbability - totalCriticalHit
            if criticalRate > 55:
               criticalRate = 55
            return criticalRate
         return currentCriticalHitProbability
      return 0
   
   @property
   def maximalRangeWithBoosts(self) -> int:
      rangeBonus:float = None
      entityId:float = self.getEntityId()
      stats:EntityStats = StatsManager().getStats(entityId)
      spellModifiers:SpellModifiers = SpellModifiersManager().getSpellModifiers(entityId, self.id)
      boostableRange:bool = self.spellLevelInfos.rangeCanBeBoosted
      finalRange:float = self.maximalRange
      if spellModifiers is not None:
         if not boostableRange:
            if spellModifiers.hasModifier(CharacterSpellModificationTypeEnum.RANGEABLE):
               boostableRange = True
         if spellModifiers.hasModifier(CharacterSpellModificationTypeEnum.RANGE_MAX):
            finalRange += spellModifiers.getModifierValue(CharacterSpellModificationTypeEnum.RANGE_MAX)
      if boostableRange and stats is not None:
         rangeBonus = stats.getStatTotalValue(StatIds.RANGE) - stats.getStatAdditionalValue(StatIds.RANGE)
         finalRange += rangeBonus
      if finalRange < self.minimalRange:
         finalRange = self.minimalRange
      return finalRange
   
   @property
   def canTargetCasterOutOfZone(self) -> bool:
      effect:EffectInstance = None
      if self._canTargetCasterOutOfZone == None:
         for effect in self.effects:
            if effect.targetMask.find("C") != -1 and effect.triggers == "I":
               self._canTargetCasterOutOfZone = True
         if not self._canTargetCasterOutOfZone:
            for effect in self.criticalEffect:
               if effect.targetMask.find("C") != -1 and effect.triggers == "I":
                  self._canTargetCasterOutOfZone = True
         if not self._canTargetCasterOutOfZone:
            self._canTargetCasterOutOfZone = False
      return self._canTargetCasterOutOfZone

   def getProperty(self, name) -> Any:
      spellModifier:SpellModifier = None
      numberToReturn:float = None
      booleanToReturn:bool = False
      build:BuildWrapper = None
      iw:ItemWrapper = None
      if isAttribute(name):
         return self[name]
      if InventoryManager().currentBuildId != -1:
         for build in InventoryManager().builds:
            if build.id == InventoryManager().currentBuildId:
         if self.id == 0:
            for iw in build.equipment:
               if isinstance(iw, WeaponWrapper):
            if isinstance(iw, WeaponWrapper):
               return self.getWeaponProperty(name,iw)
      elif self.id == 0 and PlayedCharacterManager().currentWeapon != None:
         return self.getWeaponProperty(name)
      spellModifier = None
      numberToReturn = 0
      booleanToReturn = False
      str(switch(name))
      if None  == "id":
      if None  == "nameId":
      if None  == "descriptionId":
      if None  == "typeId":
      if None  == "scriptParams":
      if None  == "scriptParamsCritical":
      if None  == "scriptId":
      if None  == "scriptIdCritical":
      if None  == "iconId":
      if None  == "spellLevels":
      if None  == "useParamCache":
      if None  == "name":
      if None  == "description":
      if None  == "variants":
      if None  == "default_zone":
            return self.spell[name]
      if None  == "spellBreed":
      if None  == "needFreeCell":
      if None  == "needTakenCell":
      if None  == "minPlayerLevel":
      if None  == "maxStack":
      if None  == "globalCooldown":
            return str(self.spellLevelInfos[name)]
      if None  == "criticalHitProbability":
            return self.getCriticalHitProbability()
      if None  == "maxCastPerTurn":
            numberToReturn = self.spellLevelInfos["maxCastPerTurn"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.MAX_CAST_PER_TURN)
            if spellModifier is not None:
               numberToReturn += spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue
            return numberToReturn
      if None  == "range":
            numberToReturn = self.spellLevelInfos["range"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.RANGE_MAX)
            if spellModifier is not None:
               numberToReturn += spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue
            return numberToReturn
      if None  == "minRange":
            numberToReturn = self.spellLevelInfos["minRange"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.RANGE_MIN)
            if spellModifier is not None:
               numberToReturn += spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue
            return numberToReturn
      if None  == "maxCastPerTarget":
            numberToReturn = self.spellLevelInfos["maxCastPerTarget"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.MAX_CAST_PER_TARGET)
            if spellModifier is not None:
               numberToReturn += spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue
            return numberToReturn
      if None  == "castInLine":
            booleanToReturn = self.spellLevelInfos["castInLine"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.CAST_LINE)
            if spellModifier is not None:
               booleanToReturn = booleanToReturn and spellModifier.totalValue == 0
            return booleanToReturn
      if None  == "castInDiagonal":
            return self.spellLevelInfos["castInDiagonal"]
      if None  == "castTestLos":
            booleanToReturn = self.spellLevelInfos["castTestLos"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.LOS)
            if spellModifier is not None:
               booleanToReturn = booleanToReturn and spellModifier.totalValue == 0
            return booleanToReturn
      if None  == "rangeCanBeBoosted":
            booleanToReturn = self.spellLevelInfos["rangeCanBeBoosted"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.RANGEABLE)
            if spellModifier is not None:
               booleanToReturn = booleanToReturn or spellModifier.totalValue > 0
            return booleanToReturn
      if None  == "apCost":
            numberToReturn = self.spellLevelInfos["apCost"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.AP_COST)
            if spellModifier is not None:
               numberToReturn += -(spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue + spellModifier.baseValue + spellModifier.additionalValue + spellModifier.alignGiftBonusValue)
            return numberToReturn
      if None  == "minCastInterval":
            numberToReturn = self.spellLevelInfos["minCastInterval"]
            spellModifier = SpellModifiersManager().getSpellModifier(getEntityId(),self.id,CharacterSpellModificationTypeEnum.CAST_INTERVAL)
            if spellModifier is not None:
               numberToReturn += -(spellModifier.contextModifValue + spellModifier.objectsAndMountBonusValue + spellModifier.baseValue + spellModifier.additionalValue + spellModifier.alignGiftBonusValue)
            return numberToReturn
      if None  == "isSpellWeapon":
            return self.id == 0
      if None  == "isDefaultSpellWeapon":
            return self.id == 0 and not PlayedCharacterManager().currentWeapon
      if None  == "statesRequired":
            return self.spellLevelInfos.statesRequired
      if None  == "statesForbidden":
            return self.spellLevelInfos.statesForbidden
      else:
            return
   
   def getWeaponProperty(self, name, item:ItemWrapper = None) -> Any:
      weapon:ItemWrapper = !not item ? item : PlayedCharacterManager().currentWeapon as ItemWrapper
      if not weapon:
         return None
      str(switch(name))
      if None  == "id":
            return 0
      if None  == "nameId":
      if None  == "descriptionId":
      if None  == "iconId":
      if None  == "name":
      if None  == "description":
      if None  == "criticalHitProbability":
      if None  == "castInLine":
      if None  == "castInDiagonal":
      if None  == "castTestLos":
      if None  == "apCost":
      if None  == "minRange":
      if None  == "range":
            return weapon[name]
      if None  == "isDefaultSpellWeapon":
      if None  == "useParamCache":
      if None  == "needTakenCell":
      if None  == "rangeCanBeBoosted":
            return False
      if None  == "isSpellWeapon":
      if None  == "needFreeCell":
            return True
      if None  == "minCastInterval":
      if None  == "minPlayerLevel":
      if None  == "maxStack":
      if None  == "maxCastPerTurn":
      if None  == "maxCastPerTarget":
            return 0
      if None  == "typeId":
            return DataEnum.SPELL_TYPE_SPECIALS
      if None  == "scriptParams":
      if None  == "scriptParamsCritical":
      if None  == "spellLevels":
            return None
      if None  == "scriptId":
      if None  == "scriptIdCritical":
      if None  == "spellBreed":
            return 0
      if None  == "variants":
            return []
      else:
            return
   
   def getCriticalHitProbability(self) -> float:
      criticalHitProbability:float = self.spellLevelInfos["criticalHitProbability"]
      return criticalHitProbability > 0 ? float(55 - criticalHitProbability) : float(Number.None)
   
   def clone(self) -> Any:
      returnSpellWrapper:SpellWrapper = None
      return SpellWrapper.create(self.id,self.spellLevel,False,self.playerId,self.variantActivated)
   
   def addHolder(self, h:ISlotDataHolder) -> None:
      self._slotDataHolderManager.addHolder(h)
   
   def setLinkedSlotData(self, slotData:ISlotData) -> None:
      self._slotDataHolderManager.setLinkedSlotData(slotData)
   
   def removeHolder(self, h:ISlotDataHolder) -> None:
      self._slotDataHolderManager.removeHolder(h)
   
   def __str__(self) -> str:
      return "[SpellWrapper #" + self.id + "]"
   
   def updateSpellLevelAccordingToPlayerLevel(self) -> None:
      i:int = 0
      currentCharacterLevel:int = PlayedCharacterManager().limitedLevel
      if not self.spell:
         return
      spellLevels:list = self._spell.spellLevelsInfo
      spellLevelsCount:int = len(spellLevels)
      index:int = 0
      for(i = spellLevelsCount - 1 i >= 0 i--)
         if currentCharacterLevel >= spellLevels[i].minPlayerLevel:
            index = i
      self._spellLevel = spellLevels[index]
      self.spellLevel = index + 1
   
   def setSpellEffects(self, areModifiers:bool = True) -> None:
      effectInstance:EffectInstance = None
      damageBaseSpellModifier:SpellModifier = None
      damageSpellModifier:SpellModifier = None
      healSpellModifier:SpellModifier = None
      modif:int = 0
      len:int = 0
      entityId:float = None
      effectInstanceDice:EffectInstanceDice = None
      self.effects = list[EffectInstance]()
      self.criticalEffect = list[EffectInstance]()
      for effectInstance in self._spellLevel.effects:
         effectInstance = effectInstance.clone()
         entityId = getEntityId()
         if areModifiers and (effectInstance.category == DataEnum.ACTION_TYPE_DAMAGES and BASE_DAMAGE_EFFECT_IDS.find(effectInstance.effectId) != -1):
            damageBaseSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.BASE_DAMAGE)
            if damageBaseSpellModifier and effectInstance is EffectInstanceDice:
               modif = damageBaseSpellModifier.totalValue - damageBaseSpellModifier.additionalValue
               effectInstance.diceNum += modif
               if effectInstance.diceSide > 0:
                  effectInstance.diceSide += modif
            damageSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.DAMAGE)
            healSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.HEAL_BONUS)
            if damageSpellModifier:
               effectInstance.modificator = damageSpellModifier.totalValue - damageSpellModifier.additionalValue
            elif healSpellModifier:
               effectInstance.modificator = healSpellModifier.totalValue - healSpellModifier.additionalValue
         self.effects.append(effectInstance)
      for effectInstance in self._spellLevel.criticalEffect:
         effectInstance = effectInstance.clone()
         if areModifiers and (effectInstance.category == DataEnum.ACTION_TYPE_DAMAGES and BASE_DAMAGE_EFFECT_IDS.find(effectInstance.effectId) != -1):
            damageBaseSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.BASE_DAMAGE)
            if damageBaseSpellModifier and effectInstance is EffectInstanceDice:
               effectInstanceDice = effectInstance as EffectInstanceDice
               modif = damageBaseSpellModifier.totalValue - damageBaseSpellModifier.additionalValue
               effectInstanceDice.diceNum += modif
               if effectInstanceDice.diceSide > 0:
                  effectInstanceDice.diceSide += modif
            damageSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.DAMAGE)
            healSpellModifier = SpellModifiersManager().getSpellModifier(entityId,self.id,CharacterSpellModificationTypeEnum.HEAL_BONUS)
            if damageSpellModifier:
               effectInstance.modificator = damageSpellModifier.totalValue - damageSpellModifier.additionalValue
            elif healSpellModifier:
               effectInstance.modificator = damageSpellModifier.totalValue - damageSpellModifier.additionalValue
         self.criticalEffect.append(effectInstance)
      len = self._splen(ellLevel.additionalEffectsZones)
      if len > 0:
         self.additionalEffectsZones = list[EffectZone](0)
      for(j:int = 0 j < len j += 2)
         self.additionalEffectsZones.append(EffectZone(self._spellLevel.additionalEffectsZones[j],self._spellLevel.additionalEffectsZones[j + 1]))
