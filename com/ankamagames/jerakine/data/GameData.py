                        
import logging
from com.ankamagames.jerakine.data.abstractDataManager import AbstractDataManager
from com.ankamagames.jerakine.data.gameDataFileAccessor import GameDataFileAccessor
from com.ankamagames.jerakine.newCache.LruGarbageCollector import LruGarbageCollector
from com.ankamagames.jerakine.newCache.impl.cache import Cache
logger = logging.getLogger("bot")



class GameData(AbstractDataManager):
   
   CACHE_SIZE_RATIO:float = 0.1
   _directObjectCaches:dict = dict()
   _objectCaches:dict = dict()
   _objectsCaches:dict = dict()
   _overrides:dict = dict()
      
   
   @classmethod
   def addOverride(cls, moduleId:str, keyId:int, newKeyId:int) -> None:
      if not cls._overrides[moduleId]:
         cls._overrides[moduleId] = []
      cls._overrides[moduleId][keyId] = newKeyId
   
   @classmethod
   def getObject(cls, moduleId:str, keyId:int) -> object:
      wr:WeakReference = None
      if cls._overrides[moduleId] and cls._overrides[moduleId][keyId]:
         keyId = cls._overrides[moduleId][keyId]
      if not cls._directObjectCaches[moduleId]:
         cls._directObjectCaches[moduleId] = dict()
      else:
         wr = cls._directObjectCaches[moduleId][keyId]
         if wr:
            o = wr.object
            if o:
               return o
      if not cls._objectCaches[moduleId]:
         cls._objectCaches[moduleId] = Cache(GameDataFileAccessor.getCount(moduleId) * cls.CACHE_SIZE_RATIO, LruGarbageCollector())
      else:
         o = cls._objectCaches[moduleId]
         if o:
            return o
      o = GameDataFileAccessor.getObject(moduleId,keyId)
      cls._directObjectCaches[moduleId][keyId] = WeakReference(o)
      cls._objectCaches[moduleId]
      return o
   
   @classmethod
   def getObjects(cls, moduleId:str) -> list:
      objects:list = None
      if cls._objectsCaches[moduleId]:
         objects = cls._objectsCaches[moduleId].object
         if objects:
            return objects
      objects = GameDataFileAccessor.getObjects(moduleId)
      cls._objectsCaches[moduleId] = SoftReference(objects)
      return objects
