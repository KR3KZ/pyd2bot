from re import S
from com.ankamagames.atouin.AtouinConstants import AtouinConstants
from com.ankamagames.atouin.data.map.Cell import Cell
from com.ankamagames.atouin.data.map.map import Map
from com.ankamagames.atouin.managers.MapDisplayManager import MapDisplayManager
from com.ankamagames.atouin.messages.AdjacentMapClickMessage import AdjacentMapClickMessage
from com.ankamagames.atouin.utils.CellIdConverter import CellIdConverter
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.types.enums.DirectionsEnum import DirectionsEnum
from com.ankamagames.jerakine.types.positions.MapPoint import Point
logger = Logger(__name__)


class FrustumManager(metaclass=Singleton):
       
   SHAPE_INSIDE_PADDING:float = 30
      
   _lastCellId:int
   
   _enable:bool
   
   def __init__(self):
      super().__init__()
   
   def init(self) -> None:
      self._lastCellId = -1
   
   def click(self, target) -> None:
      destMapId:float = None
      currentMap:Map = MapDisplayManager().getDataMapContainer().dataMap

      if target  == DirectionsEnum.RIGHT:
         destMapId = currentMap.rightNeighbourId

      if target  == DirectionsEnum.LEFT:
         destMapId = currentMap.leftNeighbourId

      if target  == DirectionsEnum.DOWN:
         destMapId = currentMap.bottomNeighbourId

      if target  == DirectionsEnum.UP:
         destMapId = currentMap.topNeighbourId

      cellData = self.findNearestCell(target)
      if cellData.cell == -1:
         return
         
      if not cellData.custom:
         self.sendClickAdjacentMsg(destMapId, cellData.cell)

      else:
         self.sendCellClickMsg(destMapId, cellData.cell)
   
   def findNearestCell(self, direction:int, currentCellId) -> object:
      cellList = list[int]()
      currentMap:Map = MapDisplayManager().getDataMapContainer().dataMap

      if direction  == DirectionsEnum.RIGHT:
         y = 1
         cellList = currentMap.rightArrowCell

      if direction  == DirectionsEnum.LEFT:
         y = 1
         cellList = currentMap.leftArrowCell

      if direction  == DirectionsEnum.DOWN:
         x = 1
         cellList = currentMap.bottomArrowCell

      if direction  == DirectionsEnum.UP:
         x = 1
         cellList = currentMap.topArrowCell

      if not cellList or not len(cellList):
         return {  
            "cell":-1,
            "distance":float("inf")
         }

      currentDist = 0

      return {
         "cell":currentCellId,
         "distance":currentDist
      }
   
   
   def findNearestBorderCellFromPoint(self, direction:int, fromCellPoint:Point) -> object:
      currentlyCheckedCellX:int = 0
      currentlyCheckedCellY:int = 0
      closestCellX:int = 0
      closestCellY:int = 0
      currentCellPixelPoint:Point = None
      currentCellZ:int = 0
      currentDistance:float = None
      i:int = 0
      maxI:int = 0
      currentCellId:int = 0
      cellData:Cell = None
      mapChangeData:int = 0
      currentMap:Map = MapDisplayManager().getDataMapContainer().dataMap
      lastSmallestDistance:float = float("inf")

      if direction  == DirectionsEnum.RIGHT:
         currentlyCheckedCellX = AtouinConstants.MAP_WIDTH - 1
         currentlyCheckedCellY = AtouinConstants.MAP_WIDTH - 1

      if direction  == DirectionsEnum.LEFT:
         currentlyCheckedCellX = 0
         currentlyCheckedCellY = 0

      if direction  == DirectionsEnum.DOWN:
         currentlyCheckedCellX = AtouinConstants.MAP_HEIGHT - 1
         currentlyCheckedCellY = -(AtouinConstants.MAP_HEIGHT - 1)

      if direction  == DirectionsEnum.UP:
         currentlyCheckedCellX = 0
         currentlyCheckedCellY = 0

      closestCustomCellData:object = self.findNearestCell(direction, fromCellPoint)

      if closestCustomCellData.cell != -1:
         lastSmallestDistance = closestCustomCellData.distance
         closestCellX = CellIdConverter.cellIdToCoord(closestCustomCellData.cell).x
         closestCellY = CellIdConverter.cellIdToCoord(closestCustomCellData.cell).y

      if direction == DirectionsEnum.RIGHT or direction == DirectionsEnum.LEFT:
         maxI = AtouinConstants.MAP_HEIGHT * 2
         for i in range(maxI):
            currentCellId = CellIdConverter.coordToCellId(currentlyCheckedCellX, currentlyCheckedCellY)
            currentCellPixelPoint = Cell.cellPixelCoords(currentCellId)
            currentCellZ = Cell(currentMap.cells[currentCellId]).floor
            currentDistance = abs(fromCellPoint.y - (currentCellPixelPoint.y - currentCellZ + AtouinConstants.CELL_HALF_HEIGHT))
            if currentDistance < lastSmallestDistance:
               cellData = currentMap.cells[currentCellId]
               mapChangeData = cellData.mapChangeData
               if mapChangeData and (direction == DirectionsEnum.RIGHT and (mapChangeData & 1 or (currentCellId + 1) % (AtouinConstants.MAP_WIDTH * 2) == 0 and mapChangeData & 2 or (currentCellId + 1) % (AtouinConstants.MAP_WIDTH * 2) == 0 and mapChangeData & 128) or direction == DirectionsEnum.LEFT and (currentlyCheckedCellX == -currentlyCheckedCellY and mapChangeData & 8 or mapChangeData & 16 or currentlyCheckedCellX == -currentlyCheckedCellY and mapChangeData & 32)):
                  closestCellX = currentlyCheckedCellX
                  closestCellY = currentlyCheckedCellY
                  lastSmallestDistance = currentDistance
            if not (i % 2):
               currentlyCheckedCellX += 1
            else:
               currentlyCheckedCellY-=1

      else:
         for i in range(AtouinConstants.MAP_WIDTH * 2):
            currentCellId = CellIdConverter.coordToCellId(currentlyCheckedCellX, currentlyCheckedCellY)
            currentCellPixelPoint = Cell.cellPixelCoords(currentCellId)
            currentDistance = abs(fromCellPoint.x - (currentCellPixelPoint.x + AtouinConstants.CELL_HALF_WIDTH))
            if currentDistance < lastSmallestDistance:
               cellData = currentMap.cells[currentCellId]
               mapChangeData = cellData.mapChangeData
               if mapChangeData and (direction == DirectionsEnum.UP and (currentCellId < AtouinConstants.MAP_WIDTH and mapChangeData & 32 or mapChangeData & 64 or currentCellId < AtouinConstants.MAP_WIDTH and mapChangeData & 128) or direction == DirectionsEnum.DOWN and (currentCellId >= AtouinConstants.MAP_CELLS_COUNT - AtouinConstants.MAP_WIDTH and mapChangeData & 2 or mapChangeData & 4 or currentCellId >= AtouinConstants.MAP_CELLS_COUNT - AtouinConstants.MAP_WIDTH and mapChangeData & 8)):
                  closestCellX = currentlyCheckedCellX
                  closestCellY = currentlyCheckedCellY
                  lastSmallestDistance = currentDistance
            if not (i % 2):
               currentlyCheckedCellX += 1
            else:
               currentlyCheckedCellY += 1
               
      if lastSmallestDistance != float("inf"):
         return {
            "cell":CellIdConverter.coordToCellId(closestCellX,closestCellY),
            "custom":lastSmallestDistance == closestCustomCellData.distance
         }
      return {
         "cell":-1,
         "custom":False
      }
   
   def sendClickAdjacentMsg(self, mapId:float, cellId:int) -> None:
      msg:AdjacentMapClickMessage = AdjacentMapClickMessage()
      msg.cellId = cellId
      msg.adjacentMapId = mapId
      Atouin().handler.process(msg)
   
   def sendCellClickMsg(self, mapId:float, cellId:int) -> None:
      msg:CellClickMessage = CellClickMessage()
      msg.cellId = cellId
      msg.id = mapId
      Atouin().handler.process(msg)
   
   def out(self, e:MouseEvent) -> None:
      n:int = 0
      Sprite(e.target).alpha = 0
      if e.target  == DirectionsEnum.RIGHT:
         n = DirectionsEnum.RIGHT

      if e.target  == DirectionsEnum.LEFT:
         n = DirectionsEnum.LEFT

      if e.target  == DirectionsEnum.DOWN:
         n = DirectionsEnum.DOWN

      if e.target  == DirectionsEnum.UP:
         n = DirectionsEnum.UP

      self._lastCellId = -1
      msg:AdjacentMapOutMessage = AdjacentMapOutMessage(n, DisplayObject(e.target))
      Atouin().handler.process(msg)
   
   def mouseMove(self, e:MouseEvent) -> None:
      n:int = 0
      if e.type == MouseEvent.MOUSE_OVER:
         Sprite(e.target).alpha = 0.1
      if e.target  == DirectionsEnum.RIGHT:
         n = DirectionsEnum.RIGHT
      if e.target  == DirectionsEnum.LEFT:
         n = DirectionsEnum.LEFT
      if e.target  == DirectionsEnum.DOWN:
         n = DirectionsEnum.DOWN
      if e.target  == DirectionsEnum.UP:
         n = DirectionsEnum.UP
      cellId:int = self.findNearestCell().target.cell
      if cellId == -1 or cellId == self._lastCellId:
         return
      self._lastCellId = cellId
      cellData:Cell = MapDisplayManager().getDataMapContainer().dataMap.cells[cellId]
      msg:AdjacentMapOverMessage = AdjacentMapOverMessage(n, DisplayObject(e.target), cellId, cellData)
      Atouin().handler.process(msg)
