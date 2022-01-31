from time import perf_counter
from types import FunctionType
from whistle import Event
from ankamagames.dofus.datacenter.items.criterion.GroupItemCriterion import GroupItemCriterion
from ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from ankamagames.dofus.modules.utils.pathFinding.world.Edge import Edge
from ankamagames.dofus.modules.utils.pathFinding.world.Node import Node
from ankamagames.dofus.modules.utils.pathFinding.world.Transition import Transition
from ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex
from ankamagames.dofus.modules.utils.pathFinding.world.WorldGraph import WorldGraph
from ankamagames.jerakine.logger.Logger import Logger
from ankamagames.jerakine.utils.displays.EnterFrameConst import EnterFrameConst
from ankamagames.jerakine.utils.displays.EnterFrameDispatcher import EnterFrameDispatcher
logger = Logger(__name__)


class AStar:
   
   dest:MapPosition
   
   closedDic:dict
   
   openList:list[Node]
   
   openDic:dict
   
   iterations:int
   
   worldGraph:WorldGraph
   
   dst:Vertex
   
   callback:FunctionType
   
   _forbiddenSubareaIds:list[int]
   
   HEURISTIC_SCALE:int = 1
   
   INDOOR_WEIGHT:int = 0
   
   MAX_ITERATION:int = 10000
      
   
   def __init__(self):
      super().__init__()
   
   def search(self, worldGraph:WorldGraph, src:Vertex, dst:Vertex, callback:FunctionType) -> None:
      if AStar.callback != None:
         raise Exception("Pathfinding already in progress")
      if src == dst:
         callback(None)
         return
      self.initForbiddenSubareaList()
      AStar.worldGraph = worldGraph
      AStar.dst = dst
      AStar.callback = callback
      self.dest = MapPosition.getMapPositionById(dst.mapId)
      self.closedDic = dict()
      self.openList = list[Node]()
      self.openDic = dict()
      self.iterations = 0
      self.openList.append(Node(src, MapPosition.getMapPositionById(src.mapId)))
      EnterFrameDispatcher.addEventListener(self.compute, EnterFrameConst.COMPUTE_ASTAR)
   
   def initForbiddenSubareaList(self) -> None:
      self._forbiddenSubareaIds = GameDataQuery.queryEquals(SubArea, "mountAutoTripAllowed", False)
   
   def stopSearch(self) -> None:
      if self.callback != None:
         self.callbackWithResult(None)
   
   def compute(self, e:Event) -> None:
      current:Node = None
      edges:list[Edge] = None
      oldLength:int = 0
      cost:int = 0
      edge:Edge = None
      existing:Node = None
      map:MapPosition = None
      manhattanDistance:int = 0
      node:Node = None
      start:int = perf_counter()
      while len(self.openList) > 0:
         if self.iterations > self.MAX_ITERATION:
            self.callbackWithResult(None)
            logger.error("Too many iterations, aborting A*")
            return
         self.iterations += 1
         current = self.openList.shift()
         self.openDic[current.vertex] = None
         if current.vertex == self.dst:
            logger.debug("Goal reached with " + str(self.iterations) + " iterations")
            self.callbackWithResult(self.buildResultPath(self.worldGraph, current))
            return
         edges = self.worldGraph.getOutgoingEdgesFromVertex(current.vertex)
         oldLength = len(self.openList)
         cost = current.cost + 1
         for edge in edges:
            if self.hasValidTransition(edge):
               if self.hasValidDestinationSubarea(edge):
                  existing = self.closedDic[edge.dst]
                  if not (existing != None and cost >= existing.cost):
                     existing = self.openDic[edge.dst]
                     if not (existing != None and cost >= existing.cost):
                        map = MapPosition.getMapPositionById(edge.dst.mapId)
                        if map == None:
                           logger.info("La map " + edge.dst.mapId + " ne semble pas exister")
                        else:
                           manhattanDistance = abs(map.posX - self.dest.posX) + abs(map.posY - self.dest.posY)
                           node = Node(edge.dst, map, cost, cost + self.HEURISTIC_SCALE * manhattanDistance + (self.INDOOR_WEIGHT if current.map.outdoor and not map.outdoor else 0), current)
                           self.openList.append(node)
                           self.openDic[node.vertex] = node
         self.closedDic[current.vertex] = current
         if oldLength < len(self.openList):
            self.openList.sort(self.orderNodes)
      self.callbackWithResult(None)
   
   @staticmethod
   def hasValidTransition(edge:Edge) -> bool:
      criterionWhiteList:list = ["Ad","DM","MI","Mk","Oc","Pc","QF","Qo","Qs","Sv"]
      valid:bool = False
      for transition in edge.transitions:
         if len(transition.criterion) != 0:
            if transition.criterion.find("&") == -1 and transition.criterion.find("|") == -1 and criterionWhiteList.find(transition.criterion.substr(0,2)) != -1:
               return False
            criterion = GroupItemCriterion(transition.criterion)
            return criterion.isRespected
         valid = True
      return valid
   
   def hasValidDestinationSubarea(self, edge:Edge) -> bool:
      fromMapId:float = edge.src.mapId
      fromSubareaId:int = MapPosition.getMapPositionById(fromMapId).subAreaId
      toMapId:float = edge.dst.mapId
      toSubareaId:int = MapPosition.getMapPositionById(toMapId).subAreaId
      if fromSubareaId == toSubareaId:
         return True
      if self._forbiddenSubareaIds.find(toSubareaId) != -1:
         return False
      return True
   
   def callbackWithResult(self, result:list[Edge]) -> None:
      cb:FunctionType = self.callback
      self.callback = None
      EnterFrameDispatcher.removeEventListener(self.compute)
      cb(result)
   
   @staticmethod
   def orderNodes(a:Node, b:Node) -> int:
      return 0 if a.heuristic == b.heuristic else (1 if a.heuristic > b.heuristic else  -1)
   
   def buildResultPath(self, worldGraph:WorldGraph, node:Node) -> list[Edge]:
      result = list[Edge]()
      while node.parent != None:
         result.append(worldGraph.getEdge(node.parent.vertex, node.vertex))
         node = node.parent
      result.reverse()
      return result
