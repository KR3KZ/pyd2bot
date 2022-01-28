                                                                                    
import logging
from com.ankamagames.jerakine.managers.storeDataManager import StoreDataManager
from com.ankamagames.jerakine.types.dataStoreType import DataStoreType
from pyd2bot.gameData.enums.dataStoreEnum import DataStoreEnum
logger = logging.getLogger("bot")


class StatsManager:

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

      
   def getInstance(self) -> StatsManager: 
      if self._self is None:
         self._self = StatsManager()
         return self._self

def setStats(stats:EntityStats) -> bool:
   if stats == None:
      logger.error("Tried to set None stats. Aborting")
      return False
   _entityStats[stats.entityId] = stats
   return True


def getStats(entityId:float) -> EntityStats:
   key:str = str(entityId)
   if not (key in _entityStats):
      return None
   return _entityStats[key]


def addRawStats(entityId:float, rawStats:list[CharacterCharacteristic]) -> None:
   rawStat:CharacterCharacteristic = None
   entityKey:str = str(entityId)
   entityStats:EntityStats = _entityStats[entityKey]
   if entityStats is None:
      entityStats = EntityStats(entityId)
      setStats(entityStats)
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


def deleteStats(entityId:float) -> bool:
   entityKey:str = str(entityId)
   if not (entityKey in _entityStats):
      logger.error("Tried to del stats for entity with ID " + entityKey + ", but none were found. Aborting")
      return False
   del _entityStats[entityKey]
   logger.info("Stats for entity with ID " + entityKey + " deleted")
   return True

