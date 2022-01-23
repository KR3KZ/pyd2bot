

# noeud utilisé pour les parcours de zones (besoin:pas de création de chemin)
from functools import lru_cache
from pyd2bot.gameData.world.map import Map, Cell
from pyd2bot.utils.pathFinding.pathFinder import PathNode
DOUBLE_MAX = 1.7976931348623158E+308


class LightMapNode(PathNode):
    MIDDLE_RIGHT_CELL_ID = 279 # (Map.CELLS_COUNT - 1) / 2
    MIDDLE_DOWN_CELL_ID = 552 # (Map.CELLS_COUNT - 1 - Map.WIDTH) + (Map.WIDTH / 2)
    MIDDLE_LEFT_CELL_ID = 280 # Map.CELLS_COUNT * (Map.HEIGHT / 2)
    MIDDLE_UP_CELL_ID = 7 # Map.WIDTH / 2
    FORBIDDEN_CELL_IDS = set(0, 14, 27, 532, 545, 559)
    _map:Map
    zones:MapZones
    currentZone:list[Cell]
    
    def __init__(self, map:Map, currentCellId:int, lastDirection:int=-1, parent:PathNode=None):
        super().__init__(id=map.id, incomingDirection=lastDirection, parent=parent)
        self.map = map
        self.zones = MapZones(map)
        self.currentZone = self.zones.getZone(currentCellId)

    def getNeighbourCellFromDirection(self, srcId:int, direction:int) -> Cell:
        """retourne la cellule voisine selon une certaine direction"""
        if (srcId // Map.WIDTH) % 2 == 0: 
            offsetId = 0
            
        else:
            offsetId = 1

        if direction == Map.RIGHT:
            destId = srcId + 1
            if destId % Map.WIDTH != 0:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.DOWN_RIGHT:
            destId = srcId + Map.WIDTH + offsetId
            if destId < Map.CELLS_COUNT and (srcId + 1) % (Map.WIDTH * 2) != 0:
                return self.map.cells[destId]
            return None
            
        elif direction == Map.DOWN :
            destId = srcId + Map.WIDTH * 2
            if destId < Map.CELLS_COUNT:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.DOWN_LEFT :
            destId = srcId + Map.WIDTH - 1 + offsetId
            if destId < Map.CELLS_COUNT and srcId % (Map.WIDTH * 2) != 0:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.LEFT :
            destId = srcId - 1
            if srcId % Map.WIDTH != 0:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.UP_LEFT :
            destId = srcId - Map.WIDTH - 1 + offsetId
            if destId >= 0 and srcId % (Map.WIDTH * 2) != 0:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.UP :
            destId = srcId - Map.WIDTH * 2
            if destId >= 0:
                return self.map.cells[destId]
            return None
        
        elif direction == Map.UP_RIGHT :
            destId = srcId - Map.WIDTH + offsetId
            if destId > 0 and (srcId + 1) % (Map.WIDTH * 2) != 0:
                return self.map.cells[destId]
            return None
        
        raise Exception("Invalid direction.")
    
    def isOutgoingPossibility(self, cellId:int, direction:int) -> bool:
        """Indicate if a cell is a possibility to go out of the current map for a certain direction"""
        if direction == Map.LEFT:
            return cellId % Map.WIDTH == 0
        
        if direction == Map.RIGHT:
            return cellId % Map.WIDTH == Map.WIDTH - 1
        
        if direction == Map.UP:
            return cellId < Map.WIDTH * 2
        
        if direction == Map.DOWN:
            return cellId > 532
        
        else: 
            raise Exception("Invalid direction for changing map.")
    
    def isForbiddenPossibility(self, cellId:int) -> bool:
        """Indicatr if a cell is in the corners of the map or not to avoid double direction"""
        return cellId in self.FORBIDDEN_CELL_IDS
    
    def getOutgoingCellId(self, direction:int) -> int:
        """Get the cell id of the cell that will be reached by going out of the current map for a certain direction"""
        middleCell = self.getMiddleCell(direction)
        mapChangeCell = self.getNearestMapChangeCell(middleCell, direction)
        return mapChangeCell
    
    def getMiddleCell(self, direction):
        """Get the middle cell of the current zone twards a certain direction"""
        if direction == Map.RIGHT: 
            middleCell = self.map.cells[self.MIDDLE_RIGHT_CELL_ID]
        elif direction == Map.DOWN:
            middleCell = self.map.cells[self.MIDDLE_DOWN_CELL_ID]
        elif direction == Map.LEFT:
            middleCell = self.map.cells[self.MIDDLE_LEFT_CELL_ID]
        elif direction == Map.UP:
            middleCell = self.map.cells[self.MIDDLE_UP_CELL_ID]
        else: 
            raise Exception("Invalid direction for changing map.")
        return middleCell
    
    def getNearestMapChangeCell(self, cell, direction):
        """Get the nearest cell that will change the map for a certain direction"""
        nearestCellId = -1
        shortestDistance = DOUBLE_MAX
        for cell in self.currentZone: 
            if cell.allowsChangementMap() and self.isOutgoingPossibility(cell.id, direction) and not self.isForbiddenPossibility(cell.id): 
                currentDistance = Cell.distanceBetween(cell, cell)
                if currentDistance == 0: # petit raccourci
                    return cell.id
                if currentDistance < shortestDistance: 
                    shortestDistance = currentDistance
                    nearestCellId = cell.id
        return nearestCellId
    
    def getNeighboursCell(self, cellId:int) -> list[Cell]:
        """Get the neighbours of a cell"""
        neighbours = list[Cell]()
        for i in range(8):
            cell = self.getNeighbourCellFromDirection(cellId, i)
            if cell is not None:
                neighbours.append(cell)
        return neighbours
    
    def setNode(self) -> None: 
        pass
    
    def getCrossingDuration(self, mode:bool) -> int: 
        return 0
    
    def toString(self) -> str: 
        return self.id + " [" + self.x + ", " + self.y + "]"
    