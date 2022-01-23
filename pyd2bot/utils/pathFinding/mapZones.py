from pyd2bot.gameData.world.map import Cell, Map


class MapZones(list[dict[int, Cell]]):
    
    def __init__(self, map:Map):
        seen = set[Cell]()
        def zone(cell: Cell) -> dict[int, Cell]:
            ret = {}
            nodes = set([cell])
            while nodes:
                cell = nodes.pop()
                seen.add(cell)
                nodes |= map.getCellNeighbours(cell.id) - seen
                ret[cell.id] = cell
            return ret
        for cell in map.cells.values():
            if cell not in seen:
                self.append(zone(cell))
        
    def inSameZone(self, cellId1:int, cellId2:int) -> bool: 
        return self.getZone(cellId1) == self.getZone(cellId2)		
    
    def getZone(self, cellId:int) -> list[Cell]:
        for zone in self:
            if cellId in zone:
                return zone
        return None