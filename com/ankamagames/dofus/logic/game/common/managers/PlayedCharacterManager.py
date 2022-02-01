from typing import TYPE_CHECKING
from com.ankamagames.dofus.internalDatacenter.mount.MountData import MountData
if TYPE_CHECKING:
   from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
   from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import WeaponWrapper

from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap
from com.ankamagames.dofus.internalDatacenter.jobs.KnownJobWrapper import KnownJobWrapper
from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import WorldPointWrapper
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import CharacterInventoryPositionEnum
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import PlayerLifeStatusEnum
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.internalDatacenter.dataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.stats.entityStats import EntityStats
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.network.protocolConstantsEnum import ProtocolConstantsEnum
from com.ankamagames.dofus.network.types.game.character.choice.characterBaseInformations import CharacterBaseInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.jerakine.interfaces.IDestroyable import IDestroyable
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.types.Callback import Callback
from com.ankamagames.jerakine.types.positions.MapPoint import Point
from damageCalculation.tools import StatIds
logger = Logger(__name__)



class PlayedCharacterManager(IDestroyable):
   
   __metaclass__ = Singleton
   
   _isPartyLeader:bool = False
   
   _followingPlayerIds:list[float]
   
   _soloIdols:list[int]
   
   _partyIdols:list[int]
      
   _infosAvailableCallbacks:list[Callback]
   
   _knownZaapMapIds:list[float]
   
   _infos:CharacterBaseInformations
   
   restrictions:ActorRestrictionsInformations
   
   realEntityLook:EntityLook
   
   characteristics:CharacterCharacteristicsInformations
   
   spellsInventory:list
   
   playerSpellList:list
   
   playerForgettableSpelldict:dict
   
   playerMaxForgettableSpellsfloat:int = -1
   
   playerShortcutList:list
   
   inventory:list['ItemWrapper']
   
   currentWeapon:'WeaponWrapper'
   
   inventoryWeight:int
   
   shopWeight:int
   
   inventoryWeightMax:int
   
   _currentMap:WorldPointWrapper
   
   previousMap:WorldPointWrapper
   
   _currentSubArea:SubArea
   
   previousSubArea:SubArea
   
   previousWorldMapId:int
   
   jobs:list
   
   isInExchange:bool = False
   
   isInHisHouse:bool = False
   
   isInHouse:bool = False
   
   isIndoor:bool = False
   
   isInHisHavenbag:bool = False
   
   isInHavenbag:bool = False
   
   currentHavenbagRooms:list[HavenBagRoomPreviewInformation]
   
   isInBreach:bool = False
   
   isInAnomaly:bool = False
   
   lastCoord:Point
   
   isInParty:bool = False
   
   state:int
   
   publicMode:bool = False
   
   isRidding:bool = False
   
   isPetsMounting:bool = False
   
   petsMount:'ItemWrapper'
   
   hasCompanion:bool = False
   
   mount:MountData
   
   isFighting:bool = False
   
   fightId:int = -1
   
   teamId:int = 0
   
   isSpectator:bool = False
   
   experiencePercent:int = 0
   
   achievementPoints:int = 0
   
   achievementPercent:int = 0
   
   waitingGifts:list
   
   speedAjust:int = 0
   
   applicationInfo:GuildApplicationInformation
   
   guildApplicationInfo:GuildInformations
   
   def __init__(self):
      self._followingPlayerIds = list[float]()
      self._soloIdols = list[int]()
      self._partyIdols = list[int]()
      self._infosAvailableCallbacks = list[Callback]()
      self.playerForgettableSpelldict = dict()
      self.lastCoord = Point(0, 0)
      self.waitingGifts = list()
      super().__init__()
   
   @property
   def id(self) -> float:
      if self.infos:
         return self.infos.id
      return 0
   
   @id.setter
   def id(self, id:float) -> None:
      if self.infos:
         self.infos.id = id
   
   @property
   def infos(self) -> CharacterBaseInformations:
      return self._infos
   
   @infos.setter
   def infos(self, pInfos:CharacterBaseInformations) -> None:
      callback:Callback = None
      self._infos = pInfos
      for callback in self._infosAvailableCallbacks:
         callback.exec()
   
   @property
   def cantMinimize(self) -> bool:
      return self.restrictions.cantMinimize
   
   @property
   def forceSlowWalk(self) -> bool:
      return self.restrictions.forceSlowWalk
   
   @property
   def cantUseTaxCollector(self) -> bool:
      return self.restrictions.cantUseTaxCollector
   
   @property
   def cantTrade(self) -> bool:
      return self.restrictions.cantTrade
   
   @property
   def cantRun(self) -> bool:
      return self.restrictions.cantRun
   
   @property
   def cantMove(self) -> bool:
      return self.restrictions.cantMove
   
   @property
   def cantBeChallenged(self) -> bool:
      return self.restrictions.cantBeChallenged
   
   @property
   def cantBeAttackedByMutant(self) -> bool:
      return self.restrictions.cantBeAttackedByMutant
   
   @property
   def cantBeAggressed(self) -> bool:
      return self.restrictions.cantBeAggressed
   
   @property
   def cantAttack(self) -> bool:
      return self.restrictions.cantAttack
   
   @property
   def cantAgress(self) -> bool:
      return self.restrictions.cantAggress
   
   @property
   def cantChallenge(self) -> bool:
      return self.restrictions.cantChallenge
   
   @property
   def cantExchange(self) -> bool:
      return self.restrictions.cantExchange
   
   @property
   def cantChat(self) -> bool:
      return self.restrictions.cantChat
   
   @property
   def cantBeMerchant(self) -> bool:
      return self.restrictions.cantBeMerchant
   
   @property
   def cantUseobject(self) -> bool:
      return self.restrictions.cantUseobject
   
   @property
   def cantUseInteractiveobject(self) -> bool:
      return self.restrictions.cantUseInteractive
   
   @property
   def cantSpeakToNpc(self) -> bool:
      return self.restrictions.cantSpeakToNPC
   
   @property
   def cantChangeZone(self) -> bool:
      return self.restrictions.cantChangeZone
   
   @property
   def cantAttackMonster(self) -> bool:
      return self.restrictions.cantAttackMonster
   
   @property
   def isInKoli(self) -> bool:
      from com.ankamagames.dofus.kernel.Kernel import Kernel
      fightContextFrame:FightContextFrame = Kernel().getWorker().getFrame(FightContextFrame)
      return fightContextFrame and fightContextFrame.isKolossium
   
   @property
   def limitedLevel(self) -> int:
      if self.infos:
         if self.infos.level > ProtocolConstantsEnum.MAX_LEVEL:
            return ProtocolConstantsEnum.MAX_LEVEL
         return self.infos.level
      return 0
   
   @property
   def currentWorldMap(self) -> WorldMap:
      if self.currentSubArea:
         return self.currentSubArea.worldmap
      return None
   
   @property
   def currentMap(self) -> WorldPointWrapper:
      return self._currentMap
   
   @property
   def currentSubArea(self) -> SubArea:
      return self._currentSubArea
   
   @property
   def currentWorldMapId(self) -> int:
      if self.currentSubArea and self.currentSubArea.worldmap:
         return self.currentSubArea.worldmap.id
      return -1
   
   @property
   def isMutated(self) -> bool:
      l:int = 0
      i:int = 0
      rpBuffs = InventoryManager().inventory.getView("roleplayBuff").content
      if rpBuffs:
         l = len(rpBuffs)
         for i in range(l):
            if rpBuffs[i] and rpBuffs[i].typeId == DataEnum.ITEM_TYPE_MUTATIONS and rpBuffs[i].position == CharacterInventoryPositionEnum.INVENTORY_POSITION_MUTATION:
               return True
      return False
   
   @property
   def isPartyLeader(self) -> bool:
      return self._isPartyLeader

   @isPartyLeader.setter
   def isPartyLeader(self, b:bool) -> None:
      if not self.isInParty:
         self._isPartyLeader = False
      else:
         self._isPartyLeader = b
   @property
   def isGhost(self) -> bool:
      return self.state == PlayerLifeStatusEnum.STATUS_PHANTOM
   
   @property
   def artworkId(self) -> int:
      return self.infos.entityLook.bonesId == int(self.infos.entityLook.skins[0]) if 1 else int(self.infos.entityLook.bonesId)
   
   @property
   def followingPlayerIds(self) -> list[float]:
      return self._followingPlayerIds
   
   @currentMap.setter
   def currentMap(self, map:WorldPointWrapper) -> None:
      if self._currentMap:
         if map.mapId != self._currentMap.mapId:
            self.previousMap = self._currentMap
            self._currentMap = map
         elif not self.isInHavenbag:
            self._currentMap.setOutdoorCoords(map.outdoorX,map.outdoorY)
         else:
            self._currentMap.setOutdoorCoords(self.previousMap.outdoorX,self.previousMap.outdoorY)
      else:
         self._currentMap = map
   
   @currentSubArea.setter
   def currentSubArea(self, area:SubArea) -> None:
      if not self._currentSubArea or area != self._currentSubArea:
         if self.currentSubArea and self.currentSubArea.worldmap:
            self.previousWorldMapId = self._currentSubArea.worldmap.id
            self.previousSubArea = self.currentSubArea
         self._currentSubArea = area
   
   @followingPlayerIds.setter
   def followingPlayerIds(self, pPlayerIds:list[float]) -> None:
      self._followingPlayerIds = pPlayerIds
   
   @property
   def soloIdols(self) -> list[int]:
      return self._soloIdols
   
   @soloIdols.setter
   def soloIdols(self, pIdols:list[int]) -> None:
      self._soloIdols = pIdols
   
   @property
   def partyIdols(self) -> list[int]:
      return self._partyIdols
   
   @partyIdols.setter
   def partyIdols(self, pIdols:list[int]) -> None:
      self._partyIdols = pIdols

   @property
   def canBeAggressedByMonsters(self) -> bool:
      stats:EntityStats = StatsManager().getStats(self.id)
      if stats == None:
         return True
      if stats.getStatTotalValue(StatIds.ENERGY_POINTS) == 0:
         return False
      return not self.restrictions.cantAttackMonster
   
   def levelDiff(self, targetLevel:int) -> int:
      diff:int = 0
      playerLevel:int = self.limitedLevel
      if targetLevel > ProtocolConstantsEnum.MAX_LEVEL:
         targetLevel = ProtocolConstantsEnum.MAX_LEVEL
      type:int = 1
      if targetLevel < playerLevel:
         type = -1
      if abs(targetLevel - playerLevel) > 20:
         diff = 1 * type
      elif targetLevel > playerLevel:
         if targetLevel / playerLevel < 1.2:
            diff = 0
         else:
            diff = 1 * type
      elif playerLevel / targetLevel < 1.2:
         diff = 0
      else:
         diff = 1 * type
      return diff
   
   def addInfosAvailableCallback(self, pCallback:Callback) -> None:
      self._infosAvailableCallbacks.append(pCallback)
   
   def jobsLevel(self) -> int:
      job:KnownJobWrapper = None
      jobsLevel:int = 0
      for job in self.jobs:
         jobsLevel += job.jobLevel
      return jobsLevel
   
   def jobsfloat(self, onlyLevelOne:bool = False) -> int:
      job:KnownJobWrapper = None
      length:int = 0
      for job in self.jobs:
         if not (job.jobLevel != 1 and onlyLevelOne):
            length += 1
      return length
   
   def updateKnownZaaps(self, knownZaapMapIds:list[float]) -> None:
      self._knownZaapMapIds = knownZaapMapIds
      KernelEventsManager().processCallback(HookList.UpdateKnownZaaps, self._knownZaapMapIds)
   
   def isZaapKnown(self, mapId:float) -> bool:
      if self._knownZaapMapIds == None or len(self._knownZaapMapIds) <= 0:
         return False
      return mapId in self._knownZaapMapIds
