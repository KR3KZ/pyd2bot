from types import FunctionType
from ankamagames.dofus.modules.utils.pathFinding.world.Edge import Edge
from ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex
from ankamagames.dofus.modules.utils.pathFinding.world.WorldGraph import WorldGraph
from com.ankamagames.atouin.data.map.CellData import CellData
from com.ankamagames.atouin.managers.MapDisplayManager import MapDisplayManager
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.modules.utils.pathfinding.astar.AStar import AStar
from com.ankamagames.dofus.modules.utils.pathfinding.tools.FileLoader import FileLoader
from com.ankamagames.dofus.modules.utils.pathFinding.tools.TimeDebug import TimeDebug
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.resources.events.ResourceLoadedEvent import ResourceLoadedEvent
logger = Logger(__name__)


class WorldPathFinder:
    
    playedCharacterManager:PlayedCharacterManager
    
    worldGraph:WorldGraph
    
    callback:FunctionType
    
    src:Vertex
    
    dst:float
    
    linkedZone:int
    
        
    def __init__(self):
        super().__init__()

    def init(self) -> None:
        if WorldPathFinder.isInitialized():
            return
        playedCharacterManager = PlayedCharacterManager()
        FileLoader.loadExternalFile(XmlConfig().getEntry("config.data.pathFinding"), WorldPathFinder.setData)
        
    def getWorldGraph(self) -> WorldGraph:
        return self.worldGraph
        
    def isInitialized(self) -> bool:
        return self.worldGraph != None

    def setData(self, e:ResourceLoadedEvent) -> None:
        worldGraph = WorldGraph(e.resource)
        
    def findPath(self, destinationMapId:float, callback:FunctionType) -> None:
        if not WorldPathFinder.isInitialized():
            callback(None)
            return
        playedCharacterManager = PlayedCharacterManager()
        logger.info("Start searching path to " + str(destinationMapId))
        TimeDebug.reset()
        playedEntity:IEntity = DofusEntities.getEntity(playedCharacterManager.id)
        if not playedEntity:
            callback(None)
            return
        playedEntityCellId:int = playedEntity.position.cellId
        playerCell:CellData = MapDisplayManager().dataMap.cells[playedEntityCellId]
        self.src = self.worldGraph.getVertex(playedCharacterManager.currentMap.mapId, playerCell.linkedZoneRP)
        if self.src == None:
            callback(None)
            return
        linkedZone = 1
        WorldPathFinder.callback = callback
        self.dst = destinationMapId
        self.next()
        
    def abortPathSearch(self) -> None:
        AStar.stopSearch()

    def onAStarComplete(self, path:list[Edge]) -> None:
        cb:FunctionType = None
        if path == None:
            next()
        else:
            logger.info("path to map " + str(self.dst) + " found in " + str(TimeDebug.getElapsedTimeInSeconds()) + "s")
            cb = self.callback
            self.callback = None
            cb(path)
        
    def next(self) -> None:
        cb:FunctionType = None
        dstV:Vertex = self.worldGraph.getVertex(self.dst, self.linkedZone)
        self.linkedZone += 1
        if dstV == None:
            logger.info("no path found to go to map " + str(self.dst))
            cb = self.callback
            self.callback = None
            cb(None)
            return
        AStar.search(self.worldGraph, self.src, dstV, self.onAStarComplete)
