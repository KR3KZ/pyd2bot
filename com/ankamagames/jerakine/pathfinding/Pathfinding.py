import math
from com.ankamagames.jerakine.map.IDataMapProvider import IDataMapProvider
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MovementPath import MovementPath
from com.ankamagames.jerakine.types.positions.PathElement import PathElement
import mapTools.MapTools as MapTools

class Pathfinding:
   
   HV_COST:int = 10
   
   DIAG_COST:int = 15
   
   HEURISTIC_COST:int = 10
   
   INFINITE_COST:int = 99999999
   
   _isInit:bool = False
   
   _parentOfCell = list[int]()
   
   _costOfCell = list[int]()
   
   _openListWeights = list[int]()
   
   _isCellClosed = list[bool]()
   
   _isEntityOnCell = list[bool]()
   
   _openList = list()
   
   
   def __init__(self):
      super().__init__()
   
   def findPath(cls, map:IDataMapProvider, start:MapPoint, end:MapPoint, allowDiag:bool = True, bAllowTroughEntity:bool = True, aNoneObstacles:bool = True) -> MovementPath:
      endCellId:int = end.cellId
      startCellId:int = start.cellId
      endX:int = end.x
      endY:int = end.y
      endCellAuxId:int = startCellId
      distanceToEnd:int = MapTools.getDistance(startCellId, endCellId)
      if not cls._isInit:
         cls._costOfCell = MapTools.mapCountCell * [None]
         cls._openListWeights = MapTools.mapCountCell * [None]
         cls._parentOfCell = MapTools.mapCountCell * [None]
         cls._isCellClosed = MapTools.mapCountCell * [None]
         cls._isEntityOnCell = MapTools.mapCountCell * [None]
         cls._openList = list()
         cls._isInit = True
      for i in range(MapTools.mapCountCell):
         cls._parentOfCell[i] = MapTools.INVALID_CELL_ID
         cls._isCellClosed[i] = False
         cls._isEntityOnCell[i] = False
      cls._openList.clear()
      map.fillEntityOnCelllist(cls._isEntityOnCell, bAllowTroughEntity)
      cls._costOfCell[startCellId] = 0
      cls._openList.append(startCellId)
      while(len(cls._openList) > 0 and cls._isCellClosed[endCellId] == False):
         minimum = cls.INFINITE_COST
         smallestCostIndex = 0
         for i in range(len(cls._openList)):
            cost = cls._openListWeights[cls._openList[i]]
            if cost <= minimum:
               minimum = cost
               smallestCostIndex = i
         parentId = cls._openList[smallestCostIndex]
         parentX = MapTools.getCellIdXCoord(parentId)
         parentY = MapTools.getCellIdYCoord(parentId)
         del cls._openList[smallestCostIndex]
         cls._isCellClosed[parentId] = True
         for y in range(parentY - 1, parentY + 2):
            for x in range(parentX - 1, parentX + 2):
               cellId = MapTools.getCellIdByCoord(x, y)
               if cellId != MapTools.INVALID_CELL_ID and cls._isCellClosed[cellId] == False and\
                   cellId != parentId and\
                       map.pointMov(x, y, bAllowTroughEntity, parentId, endCellId, aNoneObstacles) and\
                           (y == parentY or x == parentX or allowDiag and\
                               (map.pointMov(parentX, y, bAllowTroughEntity, parentId, endCellId, aNoneObstacles) or\
                               map.pointMov(x, parentY, bAllowTroughEntity, parentId, endCellId, aNoneObstacles))):
                  pointWeight = 0
                  if cellId == endCellId:
                     pointWeight = 1
                  else:
                     speed = map.getCellSpeed(cellId)
                     if bAllowTroughEntity:
                        if cls._isEntityOnCell[cellId]:
                           pointWeight = 20
                        elif speed >= 0:
                           pointWeight = 6 - speed
                        else:
                           pointWeight = 12 + abs(speed)
                     else:
                        pointWeight = 1
                        if cls._isEntityOnCell[cellId]:
                           pointWeight += 0.3
                        if MapTools.isValidCoord(x + 1, y) and cls._isEntityOnCell[MapTools.getCellIdByCoord(x + 1, y)]:
                           pointWeight += 0.3
                        if MapTools.isValidCoord(x, y + 1) and cls._isEntityOnCell[MapTools.getCellIdByCoord(x, y + 1)]:
                           pointWeight += 0.3
                        if MapTools.isValidCoord(x - 1, y) and cls._isEntityOnCell[MapTools.getCellIdByCoord(x - 1, y)]:
                           pointWeight += 0.3
                        if MapTools.isValidCoord(x, y - 1) and cls._isEntityOnCell[MapTools.getCellIdByCoord(x, y - 1)]:
                           pointWeight += 0.3
                        if (map.pointSpecialEffects(x, y) & 2) == 2:
                           pointWeight += 0.2
                  movementCost = cls._costOfCell[parentId] + (cls.HV_COST if y == parentY or x == parentX else cls.DIAG_COST) * pointWeight
                  if bAllowTroughEntity:
                     cellOnEndColumn = x + y == endX + endY
                     cellOnStartColumn = x + y == start.x + start.y
                     cellOnEndLine = x - y == endX - endY
                     cellOnStartLine = x - y == start.x - start.y
                     if not cellOnEndColumn and not cellOnEndLine or not cellOnStartColumn and not cellOnStartLine:
                        movementCost += MapTools.getDistance(cellId, endCellId)
                        movementCost += MapTools.getDistance(cellId, startCellId)
                     if x == endX or y == endY:
                        movementCost -= 3
                     if cellOnEndColumn or cellOnEndLine or x + y == parentX + parentY or x - y == parentX - parentY:
                        movementCost -= 2
                     if i == start.x or y == start.y:
                        movementCost -= 3
                     if cellOnStartColumn or cellOnStartLine:
                        movementCost -= 2
                     distanceTmpToEnd = MapTools.getDistance(cellId, endCellId)
                     if distanceTmpToEnd < distanceToEnd:
                        endCellAuxId = cellId
                        distanceToEnd = distanceTmpToEnd
                  if cls._parentOfCell[cellId] == MapTools.INVALID_CELL_ID or movementCost < cls._costOfCell[cellId]:
                     cls._parentOfCell[cellId] = parentId
                     cls._costOfCell[cellId] = movementCost
                     heuristic = cls.HEURISTIC_COST * math.sqrt((endY - y) * (endY - y) + (endX - x) * (endX - x))
                     cls._openListWeights[cellId] = heuristic + movementCost
                     if cellId not in cls._openList:
                        cls._openList.append(cellId)
      movPath:MovementPath = MovementPath()
      movPath.start = start
      if cls._parentOfCell[endCellId] == MapTools.INVALID_CELL_ID:
         endCellId = endCellAuxId
         movPath.end = MapPoint.fromCellId(endCellId)
      else:
         movPath.end = end
      cursor = endCellId
      while cursor != startCellId:
         if allowDiag:
            parent = cls._parentOfCell[cursor]
            grandParent = parent == int(MapTools.INVALID_CELL_ID) if MapTools.INVALID_CELL_ID else int(cls._parentOfCell[parent])
            grandGrandParent = int(MapTools.INVALID_CELL_ID) if grandParent == MapTools.INVALID_CELL_ID else int(cls._parentOfCell[grandParent])
            kX = MapTools.getCellIdXCoord(cursor)
            kY = MapTools.getCellIdYCoord(cursor)
            if grandParent != MapTools.INVALID_CELL_ID and MapTools.getDistance(cursor, grandParent) == 1:
               if map.pointMov(kX, kY, bAllowTroughEntity, grandParent, endCellId):
                  cls._parentOfCell[cursor] = grandParent
            elif grandGrandParent != MapTools.INVALID_CELL_ID and MapTools.getDistance(cursor, grandGrandParent) == 2:
               nextX = MapTools.getCellIdXCoord(grandGrandParent)
               nextY = MapTools.getCellIdYCoord(grandGrandParent)
               interX = kX + round((nextX - kX) / 2)
               interY = kY + round((nextY - kY) / 2)
               if map.pointMov(interX, interY, bAllowTroughEntity, cursor, endCellId) and map.pointWeight(interX, interY) < 2:
                  cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(interX, interY)
            elif grandParent != MapTools.INVALID_CELL_ID and MapTools.getDistance(cursor, grandParent) == 2:
               nextX = MapTools.getCellIdXCoord(grandParent)
               nextY = MapTools.getCellIdYCoord(grandParent)
               interX = MapTools.getCellIdXCoord(parent)
               interY = MapTools.getCellIdYCoord(parent)
               if kX + kY == nextX + nextY and kX - kY != interX - interY and not map.isChangeZone(MapTools.getCellIdByCoord(kX, kY),MapTools.getCellIdByCoord(interX, interY)) and not map.isChangeZone(MapTools.getCellIdByCoord(interX, interY),MapTools.getCellIdByCoord(nextX, nextY)):
                  cls._parentOfCell[cursor] = grandParent
               elif kX - kY == nextX - nextY and kX - kY != interX - interY and not map.isChangeZone(MapTools.getCellIdByCoord(kX, kY),MapTools.getCellIdByCoord(interX, interY)) and not map.isChangeZone(MapTools.getCellIdByCoord(interX, interY),MapTools.getCellIdByCoord(nextX, nextY)):
                  cls._parentOfCell[cursor] = grandParent
               elif kX == nextX and kX != interX and map.pointWeight(kX, interY) < 2 and map.pointMov(kX, interY, bAllowTroughEntity, cursor, endCellId):
                  cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(kX, interY)
               elif kY == nextY and kY != interY and map.pointWeight(interX, kY) < 2 and map.pointMov(interX, kY, bAllowTroughEntity, cursor, endCellId):
                  cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(interX, kY)
         movPath.addPoint(PathElement(MapPoint.fromCellId(cls._parentOfCell[cursor]), MapTools.getLookDirection8Exact(cls._parentOfCell[cursor],cursor)))
         cursor = cls._parentOfCell[cursor]
      movPath.path.reverse()
      return movPath
