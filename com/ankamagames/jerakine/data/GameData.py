                        
import logging
from com.ankamagames.jerakine.data.abstractDataManager import AbstractDataManager
from com.ankamagames.jerakine.data.gameDataFileAccessor import GameDataFileAccessor
from com.ankamagames.jerakine.newCache.LruGarbageCollector import LruGarbageCollector
from com.ankamagames.jerakine.newCache.impl.cache import Cache
from com.ankamagames.jerakine.utils.memory.SoftReference import SoftReference
from com.ankamagames.jerakine.utils.memory.WeakReference import WeakReference
logger = logging.getLogger("bot")


class GameData(AbstractDataManager):
   
   CACHE_SIZE_RATIO:float = 0.1
      
   def __init__(self):
      super().__init__()
      self._directObjectCaches:dict = dict()
      self._objectCaches:dict = dict()
      self._objectsCaches:dict = dict()
      self._overrides:dict = dict()

   def addOverride(self, moduleId:str, keyId:int, newKeyId:int) -> None:
      if not self._overrides[moduleId]:
         self._overrides[moduleId] = []
      self._overrides[moduleId][keyId] = newKeyId
   
   def getObject(self, moduleId:str, keyId:int) -> object:
      wr:WeakReference = None
      if self._overrides[moduleId] and self._overrides[moduleId][keyId]:
         keyId = self._overrides[moduleId][keyId]
      if not self._directObjectCaches[moduleId]:
         self._directObjectCaches[moduleId] = dict()
      else:
         wr = self._directObjectCaches[moduleId][keyId]
         if wr:
            o = wr.object
            if o:
               return o
      if not self._objectCaches[moduleId]:
         self._objectCaches[moduleId] = Cache(GameDataFileAccessor().getCount(moduleId) * self.CACHE_SIZE_RATIO, LruGarbageCollector())
      else:
         o = self._objectCaches[moduleId]
         if o:
            return o
      o = GameDataFileAccessor().getObject(moduleId,keyId)
      self._directObjectCaches[moduleId][keyId] = WeakReference(o)
      self._objectCaches[moduleId]
      return o
   
   def getObjects(self, moduleId:str) -> list:
      objects:list = None
      if self._objectsCaches[moduleId]:
         objects = self._objectsCaches[moduleId].object
         if objects:
            return objects
      objects = GameDataFileAccessor().getObjects(moduleId)
      self._objectsCaches[moduleId] = SoftReference(objects)
      return objects
