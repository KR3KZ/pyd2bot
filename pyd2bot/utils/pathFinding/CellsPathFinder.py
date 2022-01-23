from pyd2bot.gameData.world.map import Map, Cell
from pyd2bot.gameData.world.mapPoint import MapPoint
from pyd2bot.gameData.world.mouvementPath import MovementPath
from pyd2bot.gameData.world.pathElement import PathElement
from pyd2bot.utils.pathFinding.path import PathNode
from pyd2bot.utils.pathFinding.pathFinder import Pathfinder


class CellNode(PathNode): 
    HORIZONTAL_WALK_DURATION = 510
    VERTICAL_WALK_DURATION = 425
    DIAGONAL_WALK_DURATION = 480
    HORIZONTAL_RUN_DURATION = 255
    VERTICAL_RUN_DURATION = 150
    DIAGONAL_RUN_DURATION = 170
    
    def __init__(self, cell:Cell, lastDirection:int=-1, parent:PathNode=None):
        super().__init__(cell.id, lastDirection, parent)
        self.x = cell.x
        self.y = cell.y
        self.isAccessible = cell.isAccessibleDuringRP()
        # self.setHeuristic(self.destNode)
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
        if not mode:  # walk
            if self.incomingDirection % 2 == 0:
                if self.incomingDirection % 4 == 0: # left or right
                    return self.HORIZONTAL_WALK_DURATION
                else: # top or down
                    return self.VERTICAL_WALK_DURATION
            
            else: # other directions
                return self.DIAGONAL_WALK_DURATION
        
        else:  # run
            if self.incomingDirection % 2 == 0:
                if self.incomingDirection % 4 == 0: # left or right
                    return self.HORIZONTAL_RUN_DURATION
                else: # top or down
                    return self.VERTICAL_RUN_DURATION
            
            else: # other directions
                return self.DIAGONAL_RUN_DURATION
        
    def __str__(self) -> str: 
        if self.outGoingDirection != -1:
            return f"from {self.id} go {Map.directionToString(self.outGoingDirection)}"
        return str(self.id) + " stop"

class CellsPathfinder(Pathfinder): 
    
    def __init__(self, map:Map):
        super().__init__()
        self.map = map
    
    def getNodeFromId(self, cellId:int) -> CellNode: 
        return CellNode(self.map.cells[cellId], -1, None)

    def nodeIsInList(self, cn:CellNode, plist:list[CellNode]) -> tuple[int, PathNode]: 
        for i, pn in enumerate(plist):
            if pn.id == cn.id:
                return i, pn
        return None, None
    
    def getNeighbourNodes(self, node:CellNode) -> dict[int, CellNode]: 
        neighbours = dict[int, CellNode]()
        for direction in range(8) :
            cell = self.map.getNeighbourCellFromDirection(node.id, direction)
            if cell:
                neighbours[cell.id] = CellNode(cell, direction, node)
                neighbours[cell.id].setHeuristic(self.destNode)
        return neighbours		

    def movementPathFromArray(self, iPath:list[int]) -> MovementPath:
        mpPath = [MapPoint.fromCellId(cellId) for cellId in iPath]
        mp = MovementPath([PathElement(mpPath[i], mpPath[i].orientationTo(mpPath[i + 1])) for i in range(len(mpPath) - 1)])
        mp.append(PathElement(mpPath[-1], mp[-1].orientation))
        return mp
    
