                                                                                    
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.internalDatacenter.stats.detailedStats import DetailedStat
from com.ankamagames.dofus.internalDatacenter.stats.entityStats import EntityStats
from com.ankamagames.dofus.internalDatacenter.stats.stat import Stat
from com.ankamagames.dofus.internalDatacenter.stats.usableStat import UsableStat
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicValue import CharacterCharacteristicValue
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from com.ankamagames.jerakine.managers.storeDataManager import StoreDataManager
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.types.dataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum
logger = Logger(__name__)


class StatsManager(metaclass=Singleton):
   DEFAULT_IS_VERBOSE = False
   DATA_STORE_CATEGORY = "ComputerModule_statsManager"
   DATA_STORE_KEY_IS_VERBOSE = "statsManagerIsVerbose"


   def __init__(self):
      self._entityStats = dict()
      self._isVerbose = self.DEFAULT_IS_VERBOSE
      self._statListeners = dict()
      logger.info("Instantiating stats manager")
      self._dataStoreType = DataStoreType(self.DATA_STORE_CATEGORY, True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER)
      rawIsVerbose = StoreDataManager().getData(self._dataStoreType, self.DATA_STORE_KEY_IS_VERBOSE)
      self._isVerbose = rawIsVerbose if isinstance(rawIsVerbose, bool) else self.DEFAULT_IS_VERBOSE      

   def setStats(self, stats:EntityStats) -> bool:
      if stats == None:
         logger.error("Tried to set None stats. Aborting")
         return False
      self._entityStats[stats.entityId] = stats
      return True

   def getStats(self, entityId:float) -> EntityStats:
      return self._entityStats.get(str(entityId))

   def addRawStats(self, entityId:float, rawStats:list[CharacterCharacteristic]) -> None:
      entityStats:EntityStats = self._entityStats.get(str(entityId))
      if entityStats is None:
         entityStats = EntityStats(entityId)
         self.setStats(entityStats)
      for rawStat in rawStats:
         if isinstance(rawStat, CharacterUsableCharacteristicDetailed):
            rawUsableStat = rawStat 
            entityStat = UsableStat(
               id=rawUsableStat.characteristicId,
               basevalue=rawUsableStat.base,
               additionalValue=rawUsableStat.additional,
               objectsAndMountBonusValue=rawUsableStat.objectsAndMountBonus,
               alignGiftBonusValue=rawUsableStat.alignGiftBonus,
               contextModifValue=rawUsableStat.contextModif,
               usedValue=rawUsableStat.used
            )
         elif isinstance(rawStat, CharacterCharacteristicDetailed):
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
      entityKey = str(entityId)
      if entityKey not in self._entityStats:
         logger.error("Tried to del stats for entity with ID " + entityKey + ", but none were found. Aborting")
         return False
      del self._entityStats[entityKey]
      logger.info("Stats for entity with ID " + entityKey + " deleted")
      return True

