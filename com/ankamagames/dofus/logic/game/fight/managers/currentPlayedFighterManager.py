import logging
from com.ankamagames.dofus.datacenter.items.criterion.Item import Item
from com.ankamagames.dofus.datacenter.spells.SpellState import SpellState
from com.ankamagames.dofus.internalDatacenter.dataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.stats.entityStats import EntityStats
from com.ankamagames.dofus.logic.common.managers.statsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.misc.dofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.fight.managers.fightersStateManager import FightersStateManager
from com.ankamagames.dofus.logic.game.fight.managers.playedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.types.entities.animatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from damageCalculation.tools import StatIds
logger = logging.getLogger("bot")

class CurrentPlayedFighterManager(metaclass=Singleton):
   
   _currentFighterId:float = 0
   
   _currentFighterIsRealPlayer:bool = True
   
   _characteristicsInformationsList:dict
   
   _spellCastInFightManagerList:dict
   
   _currentSummonedCreature:dict
   
   _currentSummonedBomb:dict
   
   def __init__(self):
      self._characteristicsInformationsList = dict()
      self._spellCastInFightManagerList = dict()
      self._currentSummonedCreature = dict()
      self._currentSummonedBomb = dict()
      super().__init__()
   
   @property
   def currentFighterId(self) -> float:
      return self._currentFighterId
   
   @currentFighterId.setter
   def currentFighterId(self, id:float) -> None:
      if id == self._currentFighterId:
         return
      lastFighterId:float = self._currentFighterId
      self._currentFighterId = id
      playerManager:PlayedCharacterManager = PlayedCharacterManager()
      self._currentFighterIsRealPlayer = self._currentFighterId == playerManager.id
      lastFighterEntity:AnimatedCharacter = DofusEntities.getEntity(lastFighterId)
      if lastFighterEntity:
         lastFighterEntity.setCanSeeThrough(False)
         lastFighterEntity.setCanWalkThrough(False)
         lastFighterEntity.setCanWalkTo(False)
      currentFighterEntity:AnimatedCharacter = DofusEntities.getEntity(self._currentFighterId)
      if currentFighterEntity:
         currentFighterEntity.setCanSeeThrough(True)
         currentFighterEntity.setCanWalkThrough(True)
         currentFighterEntity.setCanWalkTo(True)
      if playerManager.isFighting:
         if playerManager.id != id or lastFighterId:
            KernelEventsManager().processCallback(FightHookList.SlaveStatsList, self.getCharacteristicsInformations())
   
   def checkPlayableEntity(self, id:float) -> bool:
      if id == PlayedCharacterManager().id:
         return True
      return self._characteristicsInformationsList.get(id) != None
   
   def isRealPlayer(self) -> bool:
      return self._currentFighterIsRealPlayer
   
   def resetPlayerSpellList(self) -> None:
      playerManager:PlayedCharacterManager = PlayedCharacterManager()
      inventoryManager:InventoryManager = InventoryManager()
      if playerManager.spellsInventory != playerManager.playerSpellList:
         logger.info("Remise à jour de la liste des sorts du joueur")
         playerManager.spellsInventory = playerManager.playerSpellList
         KernelEventsManager().processCallback(HookList.SpellListUpdate,playerManager.playerSpellList)
         if Kernel.getWorker().contains(FightSpellCastFrame):
            Kernel.getWorker().removeFrame(Kernel.getWorker().getFrame(FightSpellCastFrame))
      if inventoryManager.shortcutBarSpells != playerManager.playerShortcutList:
         inventoryManager.shortcutBarSpells = playerManager.playerShortcutList
         KernelEventsManager().processCallback(InventoryHookList.ShortcutBarViewContent,ShortcutBarEnum.SPELL_SHORTCUT_BAR)
   
   def setCharacteristicsInformations(self, id:float, characteristics:CharacterCharacteristicsInformations) -> None:
      self._characteristicsInformationsList[id] = characteristics
   
   def getCharacteristicsInformations(self, id:float = 0) -> CharacterCharacteristicsInformations:
      player:PlayedCharacterManager = PlayedCharacterManager()
      if id:
         if id == player.id:
            return player.characteristics
         return self._characteristicsInformationsList[id]
      if self._currentFighterIsRealPlayer or not player.isFighting:
         return player.characteristics
      return self._characteristicsInformationsList[self._currentFighterId]
   
   def getStats(self, targetId:float = None) -> EntityStats:
      if targetId is None:
         targetId = self._currentFighterId
      return StatsManager().getStats(targetId)
   
   def getBasicTurnDuration(self) -> int:
      apBase:float = None
      apAdditional:float = None
      apBonus:float = None
      mpBase:float = None
      mpAdditional:float = None
      mpBonus:float = None
      totalTurnDurationInSeconds:int = 15
      stats:EntityStats = self.getStats(self._currentFighterId)
      if stats:
         apBase = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         apAdditional = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         apBonus = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         mpBase = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         mpAdditional = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         mpBonus = stats.getStatBaseValue(StatIds.ACTION_POINTS)
         totalTurnDurationInSeconds += apBase + apAdditional + apBonus + mpBase + mpAdditional + mpBonus
      return totalTurnDurationInSeconds
   
   def getSpellById(self, spellId:int) -> SpellWrapper:
      spellKnown:SpellWrapper = None
      player:PlayedCharacterManager = PlayedCharacterManager()
      for spellKnown in player.spellsInventory:
         if spellKnown.id == spellId:
            return spellKnown
      return None
   
   def getSpellCastManager(self) -> SpellCastInFightManager:
      scm:SpellCastInFightManager = self._spellCastInFightManagerList[self._currentFighterId]
      if not scm:
         scm = SpellCastInFightManager(self._currentFighterId)
         self._spellCastInFightManagerList[self._currentFighterId] = scm
      return scm
   
   def getSpellCastManagerById(self, id:float) -> SpellCastInFightManager:
      scm:SpellCastInFightManager = self._spellCastInFightManagerList[id]
      if not scm:
         scm = SpellCastInFightManager(id)
         self._spellCastInFightManagerList[id] = scm
      return scm
   
   def canCastThisSpell(self, spellId:int, lvl:int, pTargetId:float = 0, result:list = None) -> bool:
      spell:Spell = Spell.getSpellById(spellId)
      spellLevel:SpellLevel = spell.getSpellLevel(lvl)
      if spellLevel == None:
         return False
      player = PlayedCharacterManager()
      if self._currentFighterIsRealPlayer:
         if spellId == 0:
            if player.currentWeapon:
               spellName = player.currentWeapon.name
            else:
               spellName = spell.name
         else:
            if spellLevel.minPlayerLevel > player.infos.level:
               return False
         characteristics = self.getCharacteristicsInformations()
         if not characteristics:
            return False
      for spellKnown in player.spellsInventory:
         if spellKnown and spellKnown.id == spellId:
            selfSpell = spellKnown
            break
      if not selfSpell:
         return False
      entityStats:EntityStats = StatsManager().getStats(self.currentFighterId)
      currentPA:int = int(entityStats.getStatTotalValue(StatIds.ACTION_POINTS)) if entityStats is not None else 0
      if spellId == 0 and player.currentWeapon != None:
         weapon = Item.getItemById(player.currentWeapon.objectGID)
         if not weapon:
            return False
         apCost = weapon.apCost
         maxCastPerTurn = weapon.maxCastPerTurn
      else:
         apCost = selfSpell.apCost
         maxCastPerTurn = selfSpell.maxCastPerTurn
      if apCost > currentPA:
         return False
      states:list = FightersStateManager().getStates(self._currentFighterId)
      if not states:
         states = list()
      for state in states:
         currentState = SpellState.getSpellStateById(state)
         if currentState.preventsFight and spellId == 0:
            return False
         if currentState.id == DataEnum.SPELL_STATE_ARCHER and spellId == 0:
            weapon2 = Item.getItemById(player.currentWeapon.objectGID)
            if weapon2.typeId != DataEnum.ITEM_TYPE_BOW:
               return False
         if spellLevel.statesForbidden and state not in spellLevel.statesForbidden:
            return False
         if currentState.preventsSpellCast:
            if not (spellLevel.statesRequired or spellLevel.statesAuthorized):
               return False
            if (not spellLevel.statesRequired or len(spellLevel.statesRequired) == 0 or state not in spellLevel.statesRequired) and (not spellLevel.statesAuthorized or len(spellLevel.statesAuthorized) == 0 or state not in spellLevel.statesAuthorized):
               return False
      for stateRequired in spellLevel.statesRequired:
         if stateRequired not in states:
            stateReq = SpellState.getSpellStateById(stateRequired)
            return False
      if not spell.bypassSummoningLimit and spellLevel.canSummon and not self.canSummon():
         return False
      if spellLevel.canBomb and not self.canBomb():
         return False
      if not player.isFighting:
         return True
      spellCastManager:SpellCastInFightManager = self.getSpellCastManager()
      spellManager:SpellManager = spellCastManager.getSpellManagerBySpellId(spellId)
      if spellManager == None:
         return True
      if maxCastPerTurn <= spellManager.numberCastThisTurn and maxCastPerTurn > 0:
         return False
      if spellManager.cooldown > 0 or selfSpell.actualCooldown > 0:
         cooldown = max(spellManager.cooldown,selfSpell.actualCooldown)
         return False
      if pTargetId != 0:
         numberCastOnTarget = spellManager.getCastOnEntity(pTargetId)
         spellModifiers = SpellModifiersManager().getSpellModifiers(self.currentFighterId,spellId)
         bonus = float(spellModifiers.getModifierValue(CharacterSpellModificationTypeEnum.MAX_CAST_PER_TARGET)) if not not spellModifiers else float(0)
         if spellLevel.maxCastPerTarget + bonus <= numberCastOnTarget and spellLevel.maxCastPerTarget > 0:
            return False
      return True
   
   def endFight(self) -> None:
      if PlayedCharacterManager().id != self._currentFighterId:
         self.currentFighterId = PlayedCharacterManager().id
         self.resetPlayerSpellList()
         self.updatePortrait(DofusEntities.getEntity(self._currentFighterId))
      self._currentFighterId = 0
      self._characteristicsInformationsList = dict()
      self._spellCastInFightManagerList = dict()
      self._currentSummonedCreature = dict()
      self._currentSummonedBomb = dict()
   
   def getCurrentSummonedCreature(self, id:float = None) -> int:
      if id is None:
         id = self._currentFighterId
      return self._currentSummonedCreature[id]
   
   def setCurrentSummonedCreature(self, value:int, id:float = None) -> None:
      if id is None:
         id = self._currentFighterId
      self._currentSummonedCreature[id] = value
   
   def getCurrentSummonedBomb(self, id:float = 0) -> int:
      if not id:
         id = self._currentFighterId
      return self._currentSummonedBomb[id]
   
   def setCurrentSummonedBomb(self, value:int, id:float = 0) -> None:
      if not id:
         id = self._currentFighterId
      self._currentSummonedBomb[id] = value
   
   def resetSummonedCreature(self, id:float = None) -> None:
      self.setCurrentSummonedCreature(0,id)
   
   def addSummonedCreature(self, id:float = None) -> None:
      self.setCurrentSummonedCreature(self.getCurrentSummonedCreature(id) + 1,id)
   
   def removeSummonedCreature(self, id:float = None) -> None:
      if self.getCurrentSummonedCreature(id) > 0:
         self.setCurrentSummonedCreature(self.getCurrentSummonedCreature(id) - 1,id)
   
   def getMaxSummonedCreature(self, id:float = None) -> int:
      stats:EntityStats = self.getStats(id)
      if stats == None:
         return 0
      return stats.getStatTotalValue(StatIds.MAX_SUMMONED_CREATURES_BOOST) - stats.getStatAdditionalValue(StatIds.MAX_SUMMONED_CREATURES_BOOST)
   
   def canSummon(self, id:float = None) -> bool:
      return self.getMaxSummonedCreature(id) > self.getCurrentSummonedCreature(id)
   
   def resetSummonedBomb(self, id:float = 0) -> None:
      self.setCurrentSummonedBomb(0,id)
   
   def addSummonedBomb(self, id:float = 0) -> None:
      self.setCurrentSummonedBomb(self.getCurrentSummonedBomb(id) + 1,id)
   
   def removeSummonedBomb(self, id:float = 0) -> None:
      if self.getCurrentSummonedBomb(id) > 0:
         self.setCurrentSummonedBomb(self.getCurrentSummonedBomb(id) - 1,id)
   
   def canBomb(self, id:float = 0) -> bool:
      return self.getMaxSummonedBomb() > self.getCurrentSummonedBomb(id)
   
   def getMaxSummonedBomb(self) -> int:
      return 3
