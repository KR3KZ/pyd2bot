                                                                                    
import logging
from com.ankamagames.dofus.internalDatacenter.stats import EntityStats
from pyd2bot.game.stats.detailedStats import DetailedStat
from pyd2bot.game.stats.stat import Stat
from pyd2bot.game.stats.usableStat import UsableStat
logger = logging.getLogger("bot")


_entityStats = {}
   

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

