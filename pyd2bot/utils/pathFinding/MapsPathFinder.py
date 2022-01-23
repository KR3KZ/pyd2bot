from pyd2bot.gameData.world.map import Cell, Map
from pyd2bot.gameData.world.mapPosition import MapPosition
from pyd2bot.utils.pathFinding.lightMapNode import LightMapNode
from pyd2bot.utils.pathFinding.pathFinder import PathNode, Pathfinder


class MapsPathfinder(Pathfinder): 
    startCellId:int
    
    def __init__(self, startCellId:int):
        self.startCellId = startCellId
    
    def getNodeFromId(self, mapId:int) -> PathNode: 
        return MapNode(mapId, -1, None, self.startCellId)   
    
    def nodeIsInList(self, node:PathNode, list:list[PathNode]) -> PathNode: 
        mn = MapNode(node)
        for pn in list:
            if pn.map == mn.map: # on peut utiliser la référence ici
                return pn
        return None
    
    def getNeighbourNodes(self, node:PathNode) -> list[PathNode]: 
        neighbours = list[PathNode]()
        for direction in range(0, 8, 2): 
            map = self.getMapFromId(MapNode(node)).map.getNeighbourMapFromDirection(direction)
            if map != None:
                neighbours.append(MapNode(map, direction, node, self.startCellId))
        
        return neighbours	
    
    
    def getMapFromId(self, mapId:int) -> Map: 
        mp = MapPosition.getMapPositionById(mapId)
        if mp == None:
            return None
        return MapsCache.loadMap(mapId)
    
    
class MapNode(LightMapNode):
            
    def __init__(self, map:Map, lastDirection:int, parent:PathNode, incomingCellId:int): 
        super().__init__(map.id, lastDirection, parent)
        self.map = map
        self.zones = MapZones(map)
        self.outgoingPossibilities = list[Cell]()
        mp = MapPosition.getMapPositionById(map.id)
        self.x = mp.posX
        self.y = mp.posY
        self.outgoingCellId = -1
        if parent != None:
            self.setParentOugoingCell()
        else:  # cellule de départ et d'arrivée
            if incomingCellId == -1: # création de path à distance
                self.currentZone = self.zones.getZone(getFirstAccessibleCellId()) # pas fiable à 100%
            else:
                self.currentZone = self.zones.getZone(incomingCellId) # s'applique aussi au noeud de destination, mais cela ne change rien
        
        self.isAccessible = self.currentZone != None
        self.setHeuristic(self.destNode)
    
    
    def __init__(mapId:int, lastDirection:int, parent:PathNode, incomingCellId:int) 
        self(MapsCache.loadMap(mapId), lastDirection, parent, incomingCellId)
    
    
    # ajoute au vecteur des possibilités de sortie de la map parente une cellule de sortie pour 
    # accéder à la map fille (d:etétermine ainsi la zone courante de cette dernière)
    def setParentOugoingCell(self, ) -> void: 
        Cell cell
        list[Cell] parentCurrentZone = ((MapNode) self.parent).currentZone
        if parentCurrentZone == None:
            throw FatalError("Invalid parent current cell.")
        for parentCell:Cell : parentCurrentZone:
            if parentCell.allowsChangementMap() && isOutgoingPossibility(parentCell.id, self.lastDirection) && !isForbiddenPossibility(parentCell.id): 
                cell = getNewCellAfterMapChangement(parentCell.id, self.lastDirection)
                if cell.isAccessibleDuringRP(): 
                    #System.out.println(tostr() + " " + Pathfinder.directionTostr(self.lastDirection) + " " + directionCellId + " " + cell)
                    self.currentZone = self.zones.getZone(cell.id)
                    ((MapNode) self.parent).outgoingPossibilities.add(parentCell)
                    return
                
            
    
    
    # retourne l'id de la première cellule accessible de la map pour les noeuds sans parent
    def getFirstAccessibleCellId(self, ) -> int: 
        for cell:Cell : self.map.cells:
            if cell.isAccessibleDuringRP():
                return cell.id
        throw FatalError("Map without available cell ! Impossible !")
    
    
    # détermine la cellule d'arrivée après un changement de map
    def getNewCellAfterMapChangement(self, srcId:int, direction:int) -> Cell: 
        switch(direction) 
            case Map.RIGHT : return self.map.cells[srcId + 1 - (Map.WIDTH - 1)]
            case Map.LEFT : return self.map.cells[srcId - 1 + (Map.WIDTH - 1)]
            case Map.UP : return self.map.cells[(srcId - Map.WIDTH * 2) + 560]
            case Map.DOWN : return self.map.cells[(srcId + Map.WIDTH * 2) - 560]
        
        throw FatalError("Invalid direction for changing map.")
    
    
    # détermine la cellule de sortie de ce noeud
    
    def setNode(self, ) -> void: 
        for cell:Cell : self.outgoingPossibilities:
            if isOutgoingPossibility(cell.id, self.direction): 
                self.outgoingCellId = getOutgoingCellId(self.direction)
                break
            
    
    
    
    def getCrossingDuration(self, mode:boolean) -> int: 
        return 1
    
    
    
    def tostr(self, ) -> str: 
        if self.direction != -1:
            return self.id + " [" + self.x + ", " + self.y + "] " + Map.directionTostr(self.direction) + " " + self.outgoingCellId
        return self.id + " [" + self.x + ", " + self.y + "]"
    

