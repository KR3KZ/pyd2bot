from com.ankamagames.jerakine.logger.Logger import Logger
import sys
from time import perf_counter
from com.ankamagames.atouin.data.map.map import Map
import com.ankamagames.atouin.utils.DataMapProvider as dmpm
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.resources.events.ResourceLoadedEvent import ResourceLoadedEvent
from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader
from com.ankamagames.jerakine.types.positions.worldPoint import WorldPoint
from pyd2bot.events.BotEventsManager import BotEventsManager

logger = Logger(__name__)


class MapDisplayManager(metaclass=Singleton):

   MEMORY_LOG:dict = dict()
   _currentMap:WorldPoint
   _mapInstanceId:float = 0
   _lastMap:WorldPoint
   _nMapLoadStart:int
   _nMapLoadEnd:int

   def __init__(self) -> None:
      self._loader = MapLoader()
      self._currentMap = None
      self.currentDataMap = None
      self._lastMap = None
      self._nMapLoadStart = 0
      self._nMapLoadEnd = 0
      self._forceReloadWithoutCache = False

   @property
   def dataMap(self):
      return self.currentDataMap

   @property
   def currentMapPoint(self) -> WorldPoint:
      return self._currentMap

   @property
   def mapInstanceId(self) -> float:
      return self._mapInstanceId

   @mapInstanceId.setter
   def mapInstanceId(self, mapId:float) -> None:
      logger.debug(f"mapInstanceId {mapId}")
      self._mapInstanceId = mapId

   def reset(self) -> None:
      self._currentMap = None
      logger.debug("mapInstanceId reset 0")
      self._mapInstanceId = 0
      self._lastMap = None

   def mapDisplayed(self) -> None:
      InteractiveCellManager().updateInteractiveCell(self.currentDataMap)

   def loadMap(self, mapId:int, forceReloadWithoutCache:bool=False) -> None:
      self.lastDataMap = self.currentDataMap
      self._forceReloadWithoutCache = forceReloadWithoutCache
      self._nMapLoadStart = perf_counter()
      map = self._loader.load(mapId)
      self._nMapLoadEnd = perf_counter()
      logger.debug("Map loaded in " + str(self._nMapLoadEnd - self._nMapLoadStart) + " seconds")
      dmpm.DataMapProvider().resetUpdatedCell()
      dmpm.DataMapProvider().resetSpecialEffects()
      self.currentDataMap = map
      self._currentMap = WorldPoint.fromMapId(map.id)
      BotEventsManager().dispatch(BotEventsManager.MAP_DATA_LOADED, ResourceLoadedEvent(resource=map))
