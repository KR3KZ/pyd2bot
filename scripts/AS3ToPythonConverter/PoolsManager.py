from com.ankamagames.jerakine.JerakineConstants import JerakineConstants
from com.ankamagames.jerakine.logger.Log import Log
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.errors.SingletonError import SingletonError
from flash.utils.getQualifiedClassName import getQualifiedClassName

class PoolsManager:
   
   logger = Logger(__name__)
   
   _self:PoolsManager
   
   
   _loadersPool:Pool
   
   _urlLoadersPool:Pool
   
   _rectanglePool:Pool
   
   _pointPool:Pool
   
   _soundPool:Pool
   
   _linkedListNodePool:Pool
   
   _jsonEncoderPool:Pool
   
   _jsonDecoderPool:Pool
   
   def __init__(self):
      super().__init__()
      if _self:
         raise SingletonError("Direct initialization of singleton is forbidden. Please access PoolsManager using the getInstance method.")
   
   def getInstance(self) -> PoolsManager:
      if _self == None:
         _self = PoolsManager()
      return _self
   
   def getLoadersPool(self) -> Pool:
      if self._loadersPool == None:
         self._loadersPool = Pool(PoolableLoader,JerakineConstants.LOADERS_POOL_INITIAL_SIZE,JerakineConstants.LOADERS_POOL_GROW_SIZE,JerakineConstants.LOADERS_POOL_WARN_LIMIT)
      return self._loadersPool
   
   def getURLLoaderPool(self) -> Pool:
      if self._urlLoadersPool == None:
         self._urlLoadersPool = Pool(PoolableURLLoader,JerakineConstants.URLLOADERS_POOL_INITIAL_SIZE,JerakineConstants.URLLOADERS_POOL_GROW_SIZE,JerakineConstants.URLLOADERS_POOL_WARN_LIMIT)
      return self._urlLoadersPool
   
   def getRectanglePool(self) -> Pool:
      if self._rectanglePool == None:
         self._rectanglePool = Pool(PoolableRectangle,JerakineConstants.RECTANGLE_POOL_INITIAL_SIZE,JerakineConstants.RECTANGLE_POOL_GROW_SIZE,JerakineConstants.RECTANGLE_POOL_WARN_LIMIT)
      return self._rectanglePool
   
   def getPointPool(self) -> Pool:
      if self._pointPool == None:
         self._pointPool = Pool(PoolablePoint,JerakineConstants.POINT_POOL_INITIAL_SIZE,JerakineConstants.POINT_POOL_GROW_SIZE,JerakineConstants.POINT_POOL_WARN_LIMIT)
      return self._pointPool
   
   def getSoundPool(self) -> Pool:
      if self._soundPool == None:
         self._soundPool = Pool(PoolableSound,JerakineConstants.SOUND_POOL_INITIAL_SIZE,JerakineConstants.SOUND_POOL_GROW_SIZE,JerakineConstants.SOUND_POOL_WARN_LIMIT)
      return self._soundPool
   
   def getLinkedListNodePool(self) -> Pool:
      if self._linkedListNodePool == None:
         self._linkedListNodePool = Pool(PoolableLinkedListNode,JerakineConstants.LINKED_LIST_NODE_POOL_INITIAL_SIZE,JerakineConstants.LINKED_LIST_NODE_POOL_GROW_SIZE,JerakineConstants.LINKED_LIST_NODE_POOL_WARN_LIMIT)
      return self._linkedListNodePool
   
   def getJSONEncoderPool(self) -> Pool:
      if self._jsonEncoderPool == None:
         self._jsonEncoderPool = Pool(PoolableJSONEncoder,JerakineConstants.JSON_ENCODER_POOL_INITIAL_SIZE,JerakineConstants.JSON_ENCODER_POOL_GROW_SIZE,JerakineConstants.JSON_ENCODER_POOL_WARN_LIMIT)
      return self._jsonEncoderPool
   
   def getJSONDecoderPool(self) -> Pool:
      if self._jsonDecoderPool == None:
         self._jsonDecoderPool = Pool(PoolableJSONDecoder,JerakineConstants.JSON_DECODER_POOL_INITIAL_SIZE,JerakineConstants.JSON_DECODER_POOL_GROW_SIZE,JerakineConstants.JSON_DECODER_POOL_WARN_LIMIT)
      return self._jsonDecoderPool
