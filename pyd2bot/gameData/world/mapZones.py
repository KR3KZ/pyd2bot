import random
from pyd2bot.gameData.world.map import Cell, Map


class MapZones(list['Zone']):
    
    def __init__(self, map:Map):
        super().__init__()
        seen = set[Cell]()
        def conxComponent(cellId) -> dict[int, Cell]:
            ret = {}
            nodes = set([cellId])
            while nodes:
                cell = nodes.pop()
                seen.add(cell)
                nodes |= map.getCellNeighbours(cell.id) - seen
                ret[cell.id] = cell
            return ret
        for cell in map.cells.values():
            if cell not in seen:
                self.append(Zone(conxComponent(cell)))
    
    def inSameZone(self, cellId1:int, cellId2:int) -> bool: 
        return self.getZone(cellId1) == self.getZone(cellId2)		
    
    def getZone(self, cellId:int) -> dict[int, Cell]:
        for zone in self:
            if cellId in zone:
                return zone
        return None


class Zone(dict[int, Cell]):

    def __init__(self, map:Map):
        super().__init__()
        self._ouGoingCells  = {}
        self._possibleDirections = []
        self.map = map

    def getOuGoingCells(self, direction:int) -> list[Cell]:
        if direction not in self._ouGoingCells:
            mapOutCells = self.map.getOutgoingCells(direction)
            self._ouGoingCells[direction] = set([cell for cell in mapOutCells if cell in self])
        return self._ouGoingCells[direction]
    
    def getRandMapChangeCellToDirection(self, direction:int):
        return random.choice(list(self.getOuGoingCells(direction)))

    def getPossibleMapChangeDirections(self):
        if not self._possibleDirections:
            self._possibleDirections = [direction for direction in range(0, 8, 2) if self.getOuGoingCells(direction)]
        return self._possibleDirections
        
    def getRandMapChangeCell(self):
        rdDir = random.choice(self._possibleDirections)
        return self.getRandMapChangeCellToDirection(rdDir)
