import logging
import random
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from com.ankamagames.atouin.data.map.map import CellData, Map
logger = logging.getLogger("bot")

class Zone(dict[int, 'Cell']):

    def __init__(self, map:'Map', cells:dict[int, 'CellData']):
        super().__init__(cells)
        self._ouGoingCells  = dict[int, list[int]]()
        self._possibleDirections = list[int]()
        self.map = map

    def getOutGoingCells(self, direction:int) -> list[int]:
        if direction not in self._ouGoingCells:
            mapOutCells = self.map.getOutgoingCells(direction)
            logger.debug(f"mapOutCells to direction {direction}: {mapOutCells}")
            self._ouGoingCells[direction] = [cellId for cellId in mapOutCells if cellId in self]
            logger.debug(f"zone OutCells to direction {direction}: {mapOutCells}")
        return self._ouGoingCells[direction]
    
    def getRandMapChangeCellIdToDirection(self, direction:int) -> int:
        return random.choice(list(self.getOutGoingCells(direction)))

    def getPossibleMapChangeDirections(self):
        if not self._possibleDirections:
            self._possibleDirections = [direction for direction in range(0, 8, 2) if self.getOutGoingCells(direction)]
        return self._possibleDirections
        
    def getRandMapChange(self) -> tuple[int, int]:
        rdDir = random.choice(self.getPossibleMapChangeDirections())
        return rdDir, self.getRandMapChangeCellIdToDirection(rdDir)

class MapZones(list[Zone]):
    
    def __init__(self, map:'Map'):
        super().__init__()
        seen = set['Cell']()
        def conxComponent(cellId) -> dict[int, 'CellData']:
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
                self.append(Zone(map, conxComponent(cell)))
    
    def inSameZone(self, cellId1:int, cellId2:int) -> bool: 
        return self.getZone(cellId1) == self.getZone(cellId2)		
    
    def getZone(self, cellId:int) -> Zone:
        for zone in self:
            if cellId in zone:
                return zone
        return None
