# noeud utilisé pour les parcours de zones (besoin:pas de création de chemin)
from com.ankamagames.atouin.data.map.map import Map, CellData
from pyd2bot.gameData.world.mapZones import MapZones
from pyd2bot.utils.pathFinding.pathFinder import PathNode
DOUBLE_MAX = 1.7976931348623158E+308


class LightMapNode(PathNode):
    MIDDLE_RIGHT_CELL_ID = 279 # (Map.CELLS_COUNT - 1) / 2
    MIDDLE_DOWN_CELL_ID = 552 # (Map.CELLS_COUNT - 1 - Map.WIDTH) + (Map.WIDTH / 2)
    MIDDLE_LEFT_CELL_ID = 280 # Map.CELLS_COUNT * (Map.HEIGHT / 2)
    MIDDLE_UP_CELL_ID = 7 # Map.WIDTH / 2
    FORBIDDEN_CELL_IDS = set([0, 14, 27, 532, 545, 559])
    

    def __init__(self, map:Map, currentCellId:int=None, incomingDirection:int=-1, parent:'LightMapNode'=None):
        super().__init__(id=map.id, incomingDirection=incomingDirection, parent=parent)
        self.map = map
        self.zones = MapZones(map)
        if currentCellId is not None:
            self.currentZone = self.zones.getZone(currentCellId)
        else:
            self.currentZone = None

    @staticmethod
    def isOutgoingPossibility(cellId:int, direction:int) -> bool:
        """Indicate if a cell is a possibility to go out of the current map for a certain direction
        """
        if direction == Map.LEFT:
            return cellId % Map.WIDTH == 0
        
        if direction == Map.RIGHT:
            return cellId % Map.WIDTH == Map.WIDTH - 1
        
        if direction == Map.UP:
            return cellId < Map.WIDTH
        
        if direction == Map.DOWN:
            return cellId >= Map.WIDTH * (Map.HEIGHT - 1)
        
        else: 
            raise Exception("Invalid direction for changing map.")
    
    def isForbiddenPossibility(self, cellId:int) -> bool:
        """Indicatr if a cell is in the corners of the map or not to avoid double direction
        """
        return cellId in self.FORBIDDEN_CELL_IDS
    

    def getOutgoingCellId(self, direction:int) -> int:
        """Get the cell id of the cell that will be reached by going out of the current map for a certain direction
        """
        middleCell = self.getMiddleCell(direction)
        mapChangeCell = self.getNearestMapChangeCell(middleCell, direction)
        return mapChangeCell
    

    def getMiddleCell(self, direction):
        """Get the middle cell of the current zone twards a certain direction
        """
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
    

    def getNearestMapChangeCell(self, cell:CellData, direction):
        """Get the nearest cell that will change the map for a certain direction
        """
        nearestCellId = -1
        shortestDistance = DOUBLE_MAX
        for zcell in self.currentZone.values(): 
            if zcell.allowsChangementMap() and self.isOutgoingPossibility(zcell.id, direction) and not self.isForbiddenPossibility(zcell.id): 
                currentDistance = CellData.distanceBetween(zcell, cell)
                if currentDistance == 0: # petit raccourci
                    return zcell.id
                if currentDistance < shortestDistance: 
                    shortestDistance = currentDistance
                    nearestCellId = zcell.id
        return nearestCellId


    def setNode(self) -> None: 
        pass
    

    def getCrossingDuration(self, mode:bool) -> int: 
        return 0
    

    def __str__(self) -> str: 
        return f"{self.id}[{self.x}, {self.y}]"
    