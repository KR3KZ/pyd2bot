import logging
from com.ankamagames.jerakine.pools.poolable import Poolable
from mx.utils.LinkedList import LinkedList
from mx.utils.LinkedListNode import LinkedListNode 
logger = logging.getLogger("bot")



class Pool:
   
   _pooledClass:object 
   _pool:LinkedList
   _growSize:int
   _warnLimit:int
   _totalSize:int
   
   def __init__(self, pooledClass:object, initialSize:int, growSize:int, warnLimit:int = 0):
      super().__init__()
      self._pooledClass = pooledClass
      if self._pooledClass == PoolableLinkedListNode:
         self._pool = LinkedList()
      else:
         self._pool = PoolLinkedList()
      self._growSize = growSize
      self._warnLimit = warnLimit
      for i in range(0, initialSize, 1):
         self._pool.unshift(self._pooledClass())
      self._totalSize = initialSize
   
   @property
   def pooledClass(self) -> object:
      return self._pooledClass
   
   @property
   def poolList(self) -> LinkedList:
      return self._pool
   
   @property
   def growSize(self) -> int:
      return self._growSize
   
   @property
   def warnLimit(self) -> int:
      return self._warnLimit
   
   def checkOut(self) -> Poolable:
      o:Poolable = None
      i:int = 0
      if len(self._pool) == 0:
         for i in range(self._growSize):
            self._pool.append(self._pooledClass())
         self._totalSize += self._growSize
         if self._warnLimit > 0 and self._totalSize > self._warnLimit:
            logger.warn("Pool of " + self._pooledClass + " size beyond the warning limit. Size: " + self._totalSize + ", limit: " + self._warnLimit + ".")
      node:LinkedListNode = self._pool.shift()
      if self._pooledClass == PoolableLinkedListNode:
         o = node
      else:
         o = node.value
         PoolsManager().getLinkedListNodePool().checkIn(node)
      return o
   
   def checkIn(self, freedobject:Poolable) -> None:
      if not freedobject:
         return
      freedobject.free()
      self._pool.append(freedobject)
