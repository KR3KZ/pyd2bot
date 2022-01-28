                                                                                    
import logging
from com.ankamagames.dofus.internalDatacenter.stats.detailedStats import DetailedStat
from com.ankamagames.dofus.internalDatacenter.stats.entityStats import EntityStats
from com.ankamagames.dofus.internalDatacenter.stats.stat import Stat
from com.ankamagames.dofus.internalDatacenter.stats.usableStat import UsableStat
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicValue import CharacterCharacteristicValue
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from com.ankamagames.jerakine.managers.storeDataManager import StoreDataManager
from com.ankamagames.jerakine.types.dataStoreType import DataStoreType
from pyd2bot.gameData.enums.dataStoreEnum import DataStoreEnum
logger = logging.getLogger("bot")


class StatsManager:
   _self = None
   _entityStats = {}
   _self:'StatsManager' = None
   DEFAULT_IS_VERBOSE = False
   DATA_STORE_CATEGORY = "ComputerModule_statsManager"
   DATA_STORE_KEY_IS_VERBOSE = "statsManagerIsVerbose"
   _dataStoreType:DataStoreType = None


   def __init__(self):
      self._entityStats = dict()
      self._isVerbose = self.DEFAULT_IS_VERBOSE
      self._statListeners = dict()
      logger.info("Instantiating stats manager")
      if self._dataStoreType is None:
         self._dataStoreType = DataStoreType(self.DATA_STORE_CATEGORY, True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER)
      rawIsVerbose = StoreDataManager.getInstance().getData(self._dataStoreType, self.DATA_STORE_KEY_IS_VERBOSE)
      self._isVerbose = rawIsVerbose if isinstance(rawIsVerbose, bool) else self.DEFAULT_IS_VERBOSE

      
   def getInstance(self) -> 'StatsManager': 
      if self._self is None:
         self._self = StatsManager()
         return self._self

   def setStats(self, stats:EntityStats) -> bool:
      if stats == None:
         logger.error("Tried to set None stats. Aborting")
         return False
      self._entityStats[stats.entityId] = stats
      return True


   def getStats(self, entityId:float) -> EntityStats:
      key:str = str(entityId)
      if not (key in self._entityStats):
         return None
      return self._entityStats[key]


   def addRawStats(self, entityId:float, rawStats:list[CharacterCharacteristic]) -> None:
      rawStat:CharacterCharacteristic = None
      entityKey:str = str(entityId)
      entityStats:EntityStats = self._entityStats[entityKey]
      if entityStats is None:
         entityStats = EntityStats(entityId)
         self.setStats(entityStats)
      rawUsableStat:CharacterUsableCharacteristicDetailed = None
      rawDetailedStat:CharacterCharacteristicDetailed = None
      entityStat:Stat = None
      for rawStat in rawStats:
         if rawStat is CharacterUsableCharacteristicDetailed:
            rawUsableStat:CharacterUsableCharacteristicDetailed = rawStat 
            entityStat = UsableStat(
               rawUsableStat.characteristicId,
               rawUsableStat.base,
               rawUsableStat.additional,
               rawUsableStat.objectsAndMountBonus,
               rawUsableStat.alignGiftBonus,
               rawUsableStat.contextModif,
               rawUsableStat.used
            )
         elif rawStat is CharacterCharacteristicDetailed:
            rawDetailedStat:CharacterCharacteristicDetailed = rawStat
            entityStat = DetailedStat(
               rawDetailedStat.characteristicId, 
               rawDetailedStat.base, 
               rawDetailedStat.additional,
               rawDetailedStat.objectsAndMountBonus,
               rawDetailedStat.alignGiftBonus,
               rawDetailedStat.contextModif
            )
         else:
            if not isinstance(rawStat, CharacterCharacteristicValue):
               continue
            entityStat = Stat(rawStat.characteristicId, rawStat.total)
         entityStats.setStat(entityStat, False)


   def deleteStats(self, entityId:float) -> bool:
      entityKey:str = str(entityId)
      if not (entityKey in self._entityStats):
         logger.error("Tried to del stats for entity with ID " + entityKey + ", but none were found. Aborting")
         return False
      del self._entityStats[entityKey]
      logger.info("Stats for entity with ID " + entityKey + " deleted")
      return True

