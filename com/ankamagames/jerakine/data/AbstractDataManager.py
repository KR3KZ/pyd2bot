import logging
import math
from xmlrpc.client import MAXINT
from com.ankamagames.jerakine import JerakineConstants
from com.ankamagames.jerakine.managers.storeDataManager import StoreDataManager
from com.ankamagames.jerakine.newCache.LruGarbageCollector import LruGarbageCollector
from com.ankamagames.jerakine.newCache.iCache import ICache
from com.ankamagames.jerakine.newCache.impl.cache import Cache
from com.ankamagames.jerakine.newCache.impl.infiniteCache import InfiniteCache
from com.ankamagames.jerakine.types.customSharedObject import CustomSharedObject
logger = logging.getLogger("bot")


class AbstractDataManager:
   
   DATA_KEY:str = "data"
   _cacheSO:ICache
   _cacheKey:ICache
   _soPrefix:str = ""
   
   
   def __init__(self):
      super().__init__()
   
   def getObject(self, key:int) -> object:
      realKey:str = self._soPrefix + str(key)
      if self._cacheKey.contains(realKey):
         return self._cacheKey.peek(realKey)
      chunkLength:int = StoreDataManager.getData(JerakineConstants.DATASTORE_FILES_INFO, self._soPrefix + "_chunkLength")
      soName:str = self._soPrefix + str(math.floor(key / chunkLength))
      if self._cacheSO.contains(soName):
         foo = self._cacheSO.peek(soName)
         v = CustomSharedObject(self._cacheSO.peek(soName)).data[self.DATA_KEY][key]
         self._cacheKey.store(realKey,v)
         return v
      so = CustomSharedObject.getLocal(soName)
      if not so or self.DATA_KEY not in so.data:
         return None
      self._cacheSO.store(soName,so)
      v = so.data[self.DATA_KEY][key]
      self._cacheKey.store(realKey,v)
      return v
   
   def getObjects(self) -> list:
      fileList:list = StoreDataManager.getData(JerakineConstants.DATASTORE_FILES_INFO, self._soPrefix + "_filelist")
      if not fileList:
         return None
      data:list = list()
      for fileNum in fileList:
         soName = self._soPrefix + fileNum
         if self._cacheSO.contains(soName):
            data = data.concat(CustomSharedObject(self._cacheSO.peek(soName)).data[self.DATA_KEY])
         else:
            so = CustomSharedObject.getLocal(soName)
            if so and self.DATA_KEY in so.data:
               self._cacheSO.store(soName,so)
               data = data.concat(so.data[self.DATA_KEY])
      return data
   
   def init(self, soCacheSize:int, keyCacheSize:int, soPrefix:str = "") -> None:
      if keyCacheSize == MAXINT:
         self._cacheKey = InfiniteCache()
      else:
         self._cacheKey = Cache.create(keyCacheSize, LruGarbageCollector(), self.__class__.__name__ + "_key")
      self._cacheSO = Cache.create(soCacheSize, LruGarbageCollector(), self.__class__.__name__ + "_so")
      self._soPrefix = soPrefix
