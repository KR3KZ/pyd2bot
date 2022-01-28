from asyncio.log import logger
import logging
from pyd2bot.gameData.mapReader import MapLoader
from com.ankamagames.atouin.data.map.map import CellData, Map
from pyd2bot.gameData.world.mapPosition import MapPosition
from pyd2bot.utils.pathFinding.cellsPathFinder import CellNode
from pyd2bot.utils.pathFinding.lightMapNode import LightMapNode
from pyd2bot.gameData.world.mapZones import MapZones
from pyd2bot.utils.pathFinding.pathFinder import PathNode, Pathfinder

logger = logging.getLogger("bot")
class MapNode(LightMapNode):
    """"Wrapper of LightMapNode"""
            
    def __init__(self, map:Map or int, incomingDirection:int=-1, parent:'MapNode'=None, incomingCellId:int=None): 
        super().__init__(map=map, currentCellId=None, incomingDirection=incomingDirection, parent=parent)
        self.parent:'MapNode' = parent
        self.outgoingPossibilities = list[CellData]()
        mp = MapPosition.getMapPositionById(map.id)
        self.x = mp.posX
        self.y = mp.posY
        self.outgoingCellId = -1
        if parent:
            self.setParentOugoingCell()
        else:
            if incomingCellId == -1:
                self.currentZone = self.zones.getZone(self.getFirstAccessibleCellId())
            else:
                self.currentZone = self.zones.getZone(incomingCellId)
        self.isAccessible = self.currentZone is not None
        
        logger.info(f"{self.id}, {self.currentZone is not None}")
        self.setHeuristic(self.destNode)
    
    @classmethod
    def fromMapId(cls, mapId:int, incomingDirection:int, parent:'MapNode', incomingCellId:int):
        return cls(MapLoader.load(mapId), incomingDirection, parent, incomingCellId)
    
    def setParentOugoingCell(self) -> None:
        """Add the current cell to parent's outgoing possibilities, detemining its current zone.
        """
        parentCurrentZone = self.parent.currentZone
        if parentCurrentZone == None:
            raise Exception("Invalid parent current cell.")
        for parentCell in parentCurrentZone.values():
            if parentCell.allowsMapChange() and MapNode.isOutgoingPossibility(parentCell.id, self.incomingDirection) and not self.isForbiddenPossibility(parentCell.id): 
                cell = self.getCellAfterMapChange(parentCell.id, self.incomingDirection)
                if cell.isAccessibleDuringRP(): 
                    self.currentZone = self.zones.getZone(cell.id)
                    self.parent.outgoingPossibilities.append(parentCell)
                    return

    def getFirstAccessibleCellId(self) -> int:
        """Return the first accessible cell id of the map.
        """
        for cell in self.map.cells.values():
            if cell.isAccessibleDuringRP():
                return cell.id
        raise Exception("Map without available cell ! Impossible !")
    
    def getCellAfterMapChange(self, srcId:int, direction:int) -> CellData:
        """Detemine the cell after a map changement.
        """
        if direction == Map.RIGHT:
            return self.map.cells[srcId - (Map.WIDTH - 1)]

        elif direction == Map.LEFT:
            return self.map.cells[srcId + (Map.WIDTH - 1)]

        elif direction == Map.UP:
            return self.map.cells[(srcId - Map.WIDTH * 2) + 560]

        elif direction == Map.DOWN:
            return self.map.cells[(srcId + Map.WIDTH * 2) - 560]
            
        raise Exception("Invalid direction for changing map.")
        
    def setNode(self) -> None:
        """Determines the outgoing cell id of the node.
        """
        for cell in self.outgoingPossibilities:
            if self.isOutgoingPossibility(cell.id, self.outGoingDirection): 
                self.outgoingCellId = self.getOutgoingCellId(self.outGoingDirection)
                break
            
    def getCrossingDuration(self, mode:bool) -> int: 
        return 1
    
    def __str__(self) -> str:
        res = f"{self.id}[{self.x}, {self.y}]"
        if self.outGoingDirection != -1:
            res += " -> " + Map.directionToString(self.outGoingDirection) + " from cell " + str(self.outgoingCellId)
        return res
    

class MapsPathfinder(Pathfinder): 
    
    def __init__(self, startCellId:int):
        self.startCellId = startCellId
    
    def getNodeFromId(self, mapId:int) -> MapNode: 
        return MapNode.fromMapId(mapId, -1, None, self.startCellId)   
    
    def getNeighbours(self, node:PathNode) -> dict[int, MapNode]: 
        neighbours = dict[int, MapNode]()
        for direction in range(0, 8, 2): 
            nMapId = self.getMapFromId(node.id).getNeighborIdFromDirection(direction)
            nMap = MapLoader.load(nMapId)
            if nMap is not None:
                neighbours[nMapId] = MapNode(nMap, direction, node, self.startCellId)
        return neighbours	
    
    def getMapFromId(self, mapId:int) -> Map: 
        mp = MapPosition.getMapPositionById(mapId)
        if mp is None:
            return None
        return MapLoader.load(mapId)
    

