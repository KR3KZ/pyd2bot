                                 
import logging
import math
from pyd2bot.jerakine import JerakineConstants
from pyd2bot.jerakine.types.CustomSharedObject import CustomSharedObject
from pyd2bot.jerakine.managers import StoreDataManager
logger = logging.getLogger("bot")
   

DATA_KEY:str = "data"
_cacheSO:ICache = None
_cacheKey:ICache = None
_soPrefix:str = ""


def getObject(key:int) -> object:
   v = None
   foo = None
   so:CustomSharedObject = None
   realKey:str = _soPrefix + key
   if _cacheKey.contains(realKey):
      return _cacheKey.peek(realKey)
   chunkLength:int = StoreDataManager.getData(JerakineConstants.DATASTORE_FILES_INFO, _soPrefix + "_chunkLength")
   soName:str = _soPrefix + math.floor(key / chunkLength)
   if _cacheSO.contains(soName):
      foo = _cacheSO.peek(soName)
      v = CustomSharedObject(_cacheSO.peek(soName)).data[DATA_KEY][key]
      _cacheKey.store(realKey,v)
      return v
   so = CustomSharedObject.getLocal(soName)
   if not so or not so.data[DATA_KEY]:
      return None
   _cacheSO.store(soName,so)
   v = so.data[DATA_KEY][key]
   _cacheKey.store(realKey,v)
   return v

def getObjects(self) -> list:
   soName:str = None
   fileNum:int = 0
   so:CustomSharedObject = None
   fileList:list = StoreDataManager.getData(JerakineConstants.DATASTORE_FILES_INFO,_soPrefix + "_filelist")
   if not fileList:
      return None
   data:list = list()
   for fileNum in fileList:
      soName = _soPrefix + fileNum
      if _cacheSO.contains(soName):
         data = data.concat(CustomSharedObject(_cacheSO.peek(soName)).data[DATA_KEY])
      else:
         so = CustomSharedObject.getLocal(soName)
         if not (not so or not so.data[DATA_KEY]):
            _cacheSO.store(soName,so)
            data = data.concat(so.data[DATA_KEY])
   return data

def init(soCacheSize:int, keyCacheSize:int, soPrefix:str = "") -> None:
   if keyCacheSize == int.MAX_VALUE:
      _cacheKey = InfiniteCache()
   else:
      _cacheKey = Cache.create(keyCacheSize,LruGarbageCollector(),getQualifiedClassName(self) + "_key")
   _cacheSO = Cache.create(soCacheSize,LruGarbageCollector(),getQualifiedClassName(self) + "_so")
   _soPrefix = soPrefix
