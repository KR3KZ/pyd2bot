from com.ankamagames.jerakine.interfaces.iDestroyable import IDestroyable
from com.ankamagames.jerakine.newCache.iCache import ICache
from com.ankamagames.jerakine.newCache.iCacheGarbageCollector import ICacheGarbageCollector
from com.ankamagames.jerakine.pools.poolable import Poolable


class UsageCountHelper(Poolable):
   ref:object
   count:int

   def __init__(self):
      super().__init__()

   def init(self, ref:object, count:int) -> 'UsageCountHelper':
      self.ref = ref
      self.count = count
      return self

   def free(self) -> None:
      self.ref = None
      self.count = 0


class LruGarbageCollector(ICacheGarbageCollector):
   
   _pool:Pool
   _usageCount:dict
   _cache:ICache
   
   def __init__(self):
      self._usageCount = dict(True)
      super().__init__()
      if not _pool:
         _pool = Pool(UsageCountHelper,500,50)
   
   @cache.setter
   def cache(self, cache:ICache) -> None:
      self._cache = cache
   
   def used(self, ref) -> None:
      if self._usageCount[ref]:
         self._usageCount[ref]+=1
      else:
         self._usageCount[ref] = 1
   
   def purge(self, bounds:int) -> None:
      obj = None
      el:UsageCountHelper = None
      poke = None
      elements:list = list()
      for obj in self._usageCount:
         elements.append(_pool.checkOut())
      elements.sortOn("count", list.NUMERIC | list.DESCENDING)
      for el in elements:
         el.free()
         _pool.checkIn(el)
      while self._cache.size > bounds and len(elements):
         poke = self._cache.extract(elements.pop().ref)
         if isinstance(poke, IDestroyable):
            poke
         if isinstance(poke, bytes):
            poke


