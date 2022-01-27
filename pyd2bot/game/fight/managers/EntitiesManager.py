import logging
from pyd2bot.game.stats.iEntity import IEntity
logger = logging.getLogger("bot")  

   
RANDOM_ENTITIES_ID_START:float = -1000000
_entitiesScheduledForDestruction:list = []
_currentRandomEntity:float = -1000000
_entities = dict[IEntity]()

def addAnimatedEntity(entityID:float, entity:IEntity, strata:int = 0) -> None:
   if _entities[entityID] != None:
      logger.warn("Entity overwriting! Entity " + entityID + " has been replaced.")
   _entities[entityID] = entity

def getEntity(entityID:float) -> IEntity:
   return _entities[entityID]

def getEntityID(entity:IEntity) -> float:
   i = None
   for i in _entities:
      if entity == _entities[i]:
         return float(i)
   return 0

def removeEntity(entityID:float) -> None:
   if _entities[entityID]:
      del _entities[entityID]
      if _entitiesScheduledForDestruction[entityID]:
         del _entitiesScheduledForDestruction[entityID]

def clearEntities() -> None:
   entityBuffer:list = []
   for id in _entities:
      entityBuffer.append(id)
   for entityId in entityBuffer:
      removeEntity(entityId)
   _entities = {}

def setEntitiesVisibility(visible:bool) -> None:
   entityBuffer:list = []
   for id in _entities:
      entityBuffer.append(id)
   for entityId in entityBuffer:
      ts = _entities[entityId]
      ts.visible = visible

def entities() -> list:
   return _entities

def entitiesScheduledForDestruction() -> list:
   return _entitiesScheduledForDestruction

def entitiesCount() -> int:
   count:int = 0
   for _ in _entities:
      count += 1
   return count

def getFreeEntityId() -> float:
   _currentRandomEntity -= 1
   while _entities[_currentRandomEntity] != None:
      _currentRandomEntity -= 1
   return _currentRandomEntity

def getEntityOnCell(cellId:int, oClass = None) -> IEntity:
   useFilter = oClass != None
   isMultiFilter:bool = useFilter and oClass is list
   for e in _entities:
      if e and e.position and e.position.cellId == cellId:
         if not isMultiFilter:
            if not useFilter or not isMultiFilter and e is oClass:
               return e
         else:
            for i in range(oClass):
               if e is oClass[i]:
                  return e
   return None

def getEntitiesOnCell(cellId:int, oClass = None) -> list:
   useFilter = oClass != None
   isMultiFilter:bool = useFilter and oClass is list
   result:list = []
   for e in _entities:
      if e and e.position and e.position.cellId == cellId:
         if not isMultiFilter:
            if not useFilter or not isMultiFilter and e is oClass:
               result.append(e)
         else:
            for cls in oClass:
               if isinstance(e, cls):
                  result.append(e)
                  break
   return result

