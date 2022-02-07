from com.ankamagames.atouin.data.map.map import Map, Cell
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MouvementPath import MovementPath
from com.ankamagames.jerakine.types.positions.PathElement import PathElement
from pyd2bot.utils.pathFinding.path import PathNode
from pyd2bot.utils.pathFinding.pathFinder import Pathfinder


class CellNode(PathNode): 
    HORIZONTAL_WALK_DURATION = 510
    VERTICAL_WALK_DURATION = 425
    DIAGONAL_WALK_DURATION = 480
    HORIZONTAL_RUN_DURATION = 255
    VERTICAL_RUN_DURATION = 150
    DIAGONAL_RUN_DURATION = 170
    
    def __init__(self, cell:Cell, lastDirection:int=-1, parent:'CellNode'=None):
        super().__init__(cell.id, lastDirection, parent)
        self.x = cell.x
        self.y = cell.y
        self.isAccessible = cell.isAccessibleDuringRP()
        if parent is not None:
            self.isAccessible = self.isAccessible and parent.floor == cell.floor
        self.floor = cell.floor
        self.checkedCells = []
    

    def checkCell(self, cell:Cell) -> bool: 
        for checkedCell in self.checkedCells:
            if checkedCell == cell:
                return False
        self.checkedCells.append(cell)
        return cell.isAccessibleDuringRP()
    
    def setNode(self): 
        pass
    
    def getCrossingDuration(self, mode:bool) -> int:
        if not mode:
            if self.incomingDirection % 2 == 0:
                if self.incomingDirection % 4 == 0:
                    return self.HORIZONTAL_WALK_DURATION
                else:
                    return self.VERTICAL_WALK_DURATION
            else:
                return self.DIAGONAL_WALK_DURATION
        else:
            if self.incomingDirection % 2 == 0:
                if self.incomingDirection % 4 == 0:
                    return self.HORIZONTAL_RUN_DURATION
                else:
                    return self.VERTICAL_RUN_DURATION
            else:
                return self.DIAGONAL_RUN_DURATION
        
    def __str__(self) -> str: 
        if self.outGoingDirection != -1:
            return f"from {self.id} go {Map.directionToString(self.outGoingDirection)}"
        return str(self.id) + " stop"

class CellsPathfinder(Pathfinder): 
    
    def __init__(self, map:Map=None):
        super().__init__()
        self.map = map
    
    def getNodeFromId(self, cellId:int) -> CellNode: 
        return CellNode(self.map.cells[cellId], -1, None)

    def nodeIsInList(self, cn:CellNode, plist:list[CellNode]) -> tuple[int, PathNode]: 
        for i, pn in enumerate(plist):
            if pn.id == cn.id:
                return i
        return None, None
    
    def getNeighbours(self, node:CellNode) -> dict[int, CellNode]: 
        neighbours = dict[int, CellNode]()
        for direction in range(8) :
            cell = self.map.getNeighbourCellFromDirection(node.id, direction)
            if cell:
                neighbours[cell.id] = CellNode(cell, direction, node)
        return neighbours	

    def getAccessibleNeighbours(self, node:CellNode) -> dict[int, CellNode]: 
        neighbours = dict[int, CellNode]()
        for direction in range(8) :
            cell = self.map.getNeighbourCellFromDirection(node.id, direction)
            if cell:
                cn = CellNode(cell, direction, node)
                if cn.isAccessible:
                    neighbours[cell.id] = CellNode(cell, direction, node)
        return neighbours	

    def movementPathFromArray(self, iPath:list[int]) -> MovementPath:
        if not iPath:
            return None
        mpPath = [MapPoint.fromCellId(cellId) for cellId in iPath]
        mp = MovementPath([PathElement(mpPath[i], mpPath[i].orientationTo(mpPath[i + 1])) for i in range(len(mpPath) - 1)])
        mp.append(PathElement(mpPath[-1], mp[-1]._nOrientation))
        return mp
    
