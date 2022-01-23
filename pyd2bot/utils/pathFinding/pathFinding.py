
# représente une direction composée du sens et de la cellule sortante de la map
import random
from pyd2bot.gameData.world.map import Map
from pyd2bot.gameData.world.mapPoint import MapPoint
from pyd2bot.gameData.world.mouvementPath import MovementPath
from pyd2bot.utils.pathFinding.CellsPathFinder import CellsPathfinder
from pyd2bot.utils.pathFinding.lightMapNode import LightMapNode
from pyd2bot.utils.pathFinding.path import Path


class Direction:
    direction:int
    outgoingCellId:int
    
    def __init__(self, direction:int, outgoingCellId:int):
        self.direction = direction
        self.outgoingCellId = outgoingCellId
        
class Pathfinding:
    mapNode:LightMapNode
    currentCellId:int
    currentCellsPath:Path
    currentMapsPath:Path
    areaId:int
    lastDirection:int
    neighbourMaps:dict[int, int] 
    
    def __init__(self):
        self.currentCellId = -1
        self.lastDirection = -1
        self.areaId = -1
        self.neighbourMaps = dict[int, int]
    
    def updatePosition(self, map:Map, currentCellId:int) -> None: 
        """met à jour la position du personnage sur la map"""
        self.mapNode = LightMapNode(map, currentCellId)
        self.currentCellId = currentCellId
    
    def updatePosition(self, currentCellId:int) -> None:
        """"met à jour la position du personnage sur la map"""
        self.currentCellId = currentCellId
    
    def setArea(self, areaId:int) -> None:
        """modifie l'aire cible et calcule si nécessaire un chemin vers cette aire"""
        self.areaId = areaId
        if self.mapNode.map.subareaId != areaId:
            self.currentMapsPath = PathsCache.toArea(self.areaId, self.mapNode.map.id, self.currentCellId)
    
    def setTargetMap(self, mapId:int) -> None: 
        """modifie la map cible et calcule si nécessaire un chemin vers cette map"""
        self.currentMapsPath = PathsCache.toMap(mapId, self.mapNode.map.id, self.currentCellId)
    
    def getCellsPathTo(self, targetId:int) -> list[int]:
        """retourne un chemin de cellules vers une cellule cible"""
        pathfinder = CellsPathfinder(self.mapNode.map)
        self.currentCellsPath = pathfinder.compute(self.currentCellId, targetId)
        if self.currentCellsPath is None:
            return None
        mvPath:MovementPath = CellsPathfinder.movementPathFromArray(self.currentCellsPath.getIdsList())
        mvPath.start = MapPoint.fromCellId(self.currentCellId)
        mvPath.end = MapPoint.fromCellId(targetId)
        return mvPath.getServerMovement()
    
    def getCellsPathDuration(self, ) -> int:
        """retourne la durée du chemin de cellules"""
        return self.currentCellsPath.getCrossingDuration()
    
    def nextDirectionForReachTarget(self) -> Direction:
        """retourne une direction vers la map cible"""
        if self.currentMapsPath == None:
            return None
        return self.currentMapsPath.nextDirection()
    
    def nextDirectionInArea(self) -> Direction:
        """retourne une direction vers l'aire cible"""
        if self.mapNode.map.subareaId != self.areaId:
            raise Exception("Bad current area.")
                
        # on tire une direction au hasard s'il n'y a pas de dernière direction
        if self.lastDirection == -1:
            self.lastDirection = random.randint(0, 4) * 2
        
        # on récupère chaque map voisine
        for direction in range(0, 8, 2):
            self.neighbourMaps[direction] = self.mapNode.map.getNeighbourMapFromDirection(direction)

        # on retire la map voisine correspondant à la map précédente pour éviter les retours en arrière
        incomingDirection = self.getOppositeDirection(self.lastDirection)
        del self.neighbourMaps[incomingDirection]
        
        # il reste donc 3 directions possibles
        neighboursCount = len(self.neighbourMaps)
        while neighboursCount > 0: 
            # on récupère la map voisine correspondant à une direction au hasard
            direction = random.randint(0, neighboursCount - 1)
            randDirection = list(self.neighbourMaps.keys())[direction]
            mapId = self.neighbourMaps.get(randDirection)
            map = MapsCache.loadMap(mapId)
            
            # si la map existe et qu'elle est dans la même aire
            if map != None and map.mapType == 0 and map.subareaId == self.mapNode.map.subareaId: 
                # on tente de déterminer la cellule de changement de map
                mapChangementCell = self.mapNode.getOutgoingCellId(randDirection)
                if mapChangementCell != -1: 
                    self.lastDirection = randDirection
                    return Direction(self.lastDirection, mapChangementCell)

            del self.neighbourMaps[randDirection]
        
        
        # si aucune de ces 3 directions n'est atteignable, on fait marche arrière
        self.lastDirection = incomingDirection
        return Direction(self.lastDirection, self.mapNode.getOutgoingCellId(self.lastDirection))
    
    def getOppositeDirection(self, direction:int) -> int: 
        """retourne la direction opposée"""
        if direction >= 4:
            return direction - 4
        else:
            return direction + 4
    
    
    def toMap(self, targetMapId:int, sourceMapId:int, startCellId:int) -> Path:
        pf = MapsPathfinder(startCellId);
        Path path = pf.compute(sourceMapId, targetMapId);
        if(path == null)
            throw new FatalError("Impossible to find a path between the map with id = " + sourceMapId + " and the map with id = " + targetMapId + ".");
        path.startCellId = startCellId;
        return path
    
    
    protected static Path toArea(int areaId, int sourceMapId, int startCellId) {
        if(DEBUG)
            Log.info("Going to area with id = " + areaId + " from  " + MapPosition.getMapPositionById(sourceMapId) + ".");
        MapPosition[] mapPositions = MapPosition.getMapPositions();
        Vector<MapPosition> mapPositionsInArea = new Vector<MapPosition>();
        for(MapPosition mapPosition : mapPositions)
            if(mapPosition.subAreaId == areaId)
                mapPositionsInArea.add(mapPosition);
        if(mapPositionsInArea.size() == 0)
            throw new FatalError("Invalid area id.");
        if(DEBUG)
            Log.info(mapPositionsInArea.size() + " maps in the area with id = " + areaId + ".");
        Pathfinder pathfinder = new MapsPathfinder(startCellId);
        Path bestPath = null;
        Path tmpPath;
        int shortestDistance = 999999;
        int tmpDistance;
        for(MapPosition mapPosition : mapPositionsInArea) {
            if(mapPosition.worldMap < 1)
                continue;
            tmpPath = pathfinder.compute(sourceMapId, mapPosition.id);
            if(tmpPath == null) // chemin impossible
                continue;
            tmpDistance = tmpPath.getCrossingDuration(); // c'est en fait la distance
            if(tmpDistance < shortestDistance) {
                shortestDistance = tmpDistance;
                bestPath = tmpPath;
            }
        }
        if(bestPath != null)
            bestPath.startCellId = startCellId;
        return bestPath;
    }