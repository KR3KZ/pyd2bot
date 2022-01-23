from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.gameData.world.map import Cell, Map
from pyd2bot.gameData.world.mapPosition import MapPosition
from pyd2bot.utils.pathFinding.lightMapNode import LightMapNode
from pyd2bot.utils.pathFinding.mapZones import MapZones
from pyd2bot.utils.pathFinding.pathFinder import PathNode, Pathfinder

class MapNode(LightMapNode):
    """"Wrapper of LightMapNode"""
            
    def __init__(self, map:Map or int, incomingDirection:int, parent:PathNode, incomingCellId:int): 
        super().__init__(map=map, currentCellId=None, incomingDirection=incomingDirection, parent=parent)
        self.outgoingPossibilities = list[Cell]()
        mp = MapPosition.getMapPositionById(map.id)
        self.x = mp.posX
        self.y = mp.posY
        self.outgoingCellId = -1
        if parent:
            self.setParentOugoingCell()
        else:  # cellule de départ et d'arrivée
            if incomingCellId == -1: # création de path à distance
                self.currentZone = self.zones.getZone(self.getFirstAccessibleCellId()) # pas fiable à 100%
            else:
                self.currentZone = self.zones.getZone(incomingCellId) # s'applique aussi au noeud de destination, mais cela ne change rien
        self.isAccessible = self.currentZone != None
        self.setHeuristic(self.destNode)
    
    @classmethod
    def fromMapId(cls, mapId:int, incomingDirection:int, parent:PathNode, incomingCellId:int):
        return cls(MapLoader.load(mapId), incomingDirection, parent, incomingCellId)
    
    def setParentOugoingCell(self) -> None:
        """Add the current cell to parent's outgoing possibilities, detemining its current zone.
        """
        parentCurrentZone = MapNode(self.parent).currentZone
        if parentCurrentZone == None:
            raise Exception("Invalid parent current cell.")
        for parentCell in parentCurrentZone:
            if parentCell.allowsChangementMap() and self.isOutgoingPossibility(parentCell.id, self.incomingDirection) and not self.isForbiddenPossibility(parentCell.id): 
                cell = self.getNewCellAfterMapChangement(parentCell.id, self.incomingDirection)
                if cell.isAccessibleDuringRP(): 
                    self.currentZone = self.zones.getZone(cell.id)
                    MapNode(self.parent).outgoingPossibilities.append(parentCell)
                    return
    
    def getFirstAccessibleCellId(self) -> int:
        """Return the first accessible cell id of the map.
        """
        for cell in self.map.cells.values():
            if cell.isAccessibleDuringRP():
                return cell.id
        raise Exception("Map without available cell ! Impossible !")
    
    def getNewCellAfterMapChangement(self, srcId:int, direction:int) -> Cell:
        """Detemine the cell after a map changement.
        """
        if direction == Map.RIGHT:
            return self.map.cells[srcId + 1 - (Map.WIDTH - 1)]
        elif direction == Map.LEFT:
            return self.map.cells[srcId - 1 + (Map.WIDTH - 1)]
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
        if self.outGoingDirection != -1:
            return self.id + " [" + self.x + ", " + self.y + "] " + Map.directionToString(self.outGoingDirection) + " " + self.outgoingCellId
        return self.id + " [" + self.x + ", " + self.y + "]"
    

class MapsPathfinder(Pathfinder): 
    
    def __init__(self, startCellId:int):
        self.startCellId = startCellId
    
    def getNodeFromId(self, mapId:int) -> PathNode: 
        return MapNode(mapId, -1, None, self.startCellId)   
    
    def nodeIsInList(self, node:MapNode, list:list[MapNode]) -> tuple[int, MapNode]: 
        for i, pn in enumerate(list):
            if pn.map == node.map: # on peut utiliser la référence ici
                return i, pn
        return None, None
    
    def getNeighbourNodes(self, node:PathNode) -> list[PathNode]: 
        neighbours = list[PathNode]()
        for direction in range(0, 8, 2): 
            map = self.getMapFromId(node.id).getNeighbourMapFromDirection(direction)
            if map is not None:
                neighbours.append(MapNode(map, direction, node, self.startCellId))
        return neighbours	
    
    def getMapFromId(self, mapId:int) -> Map: 
        mp = MapPosition.getMapPositionById(mapId)
        if mp == None:
            return None
        return MapLoader.load(mapId)
    

