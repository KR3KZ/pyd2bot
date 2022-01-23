

import math

from pyd2bot.utils.pathFinding.path import Path


class PathNode:
    
    def __init__(self, id:int, incomingDirection:int, parent:'PathNode'):
        self.id = id
        self.parent = parent
        self.incomingDirection = incomingDirection
        self.outGoingDirection = -1
        self.isAccessible:bool = None
        self.x:float = None
        self.y:float = None
        self.g:float = None # distance [noeud courant / parent]
        self.f:float = None # distance [noeud courant / parent] + [noeud courant / noeud cible]
        self.h:float = None # distance [noeud courant / cible]
        self.cost:int = None  # nombre de noeuds traversés
        self.destNode:PathNode = None
        self.outgoingCellId:int = None # uniquement pour les MapNodes
        
    def setHeuristic(self, destNode:'PathNode') -> None: 
        if self.parent: 
            self.g = self.parent.g + self.distanceTo(self.parent)
            self.cost = self.parent.cost + 1
        
        else:  # noeud initial et noeud final
            self.g = 0
            self.cost = 0
        
        if destNode: 
            self.h = self.distanceTo(destNode)
            self.f = self.g + self.h
    
    def distanceTo(self, node:'PathNode') -> float: 
        return math.sqrt(math.pow(node.x - self.x, 2) + math.pow(node.y - self.y, 2))
    
    def __eq__(self, node:'PathNode') -> bool: 
        return self.id == node.id
    
    def setNode(self) -> None:
        pass
    
    def getCrossingDuration(self, mode:bool) -> int:
        pass
    
    def __str__(self):
        pass


class Pathfinder:
    currentNode:PathNode
    destNode:PathNode
    path:Path
    openedList:list[PathNode]
    closedList:list[PathNode]
    
    def getNodeFromId(self, id:int) -> PathNode:
        pass
    
    def nodeIsInList(self, node:PathNode, nlist:list[PathNode]) -> tuple[int, PathNode]:
        pass
    
    def getNeighbourNodes(self, node:PathNode) -> list[PathNode]:
        pass
    
    def compute(self, srcId:int, destId:int) -> Path: 
        currentNode = self.getNodeFromId(srcId)
        if currentNode is None:
            raise Exception("Invalid current node id.")
        destNode = self.getNodeFromId(destId)
        if destNode is None:
            raise Exception("Invalid destination node id.")
        openedList = list[PathNode]()
        closedList = list[PathNode]()
        
        while currentNode != destNode: 
            neighbours:list[PathNode] = self.getNeighbourNodes(currentNode)
            for neighbourNode in neighbours: 
                if neighbourNode.isAccessible: # skip obstacles
                    if self.nodeIsInList(neighbourNode, closedList): # already visited all its neighbours
                        continue	
                    
                    idx, node = self.nodeIsInList(neighbourNode, openedList)
                    if node:  # already visited
                        if neighbourNode.g < node.g:
                            openedList[idx] = neighbourNode # update distance
                             
                    else:
                        openedList.append(neighbourNode)	
            
            closedList.append(currentNode)
            currentNode = self.popBestNodeOfList(openedList)
            if currentNode is None: # no path found
                return None
        
        path = Path()
        direction = -2
        while currentNode: 
            if direction != -2: # -2 corresponds to the destination node
                currentNode.outGoingDirection = direction
            currentNode.setNode() # finds the outgoing cell (only for MapNodes)
            direction = currentNode.incomingDirection
            path.append(currentNode)
            currentNode = currentNode.parent
        
        path.reverse()
        return path
    
    @staticmethod
    def findBestNode(nlist:list[PathNode]):
        if len(nlist) == 0:
            return None
        currNodeIdx = 0
        for i, listNode in enumerate(nlist): 
            if listNode.f < nlist[currNoneIdx].f:
                currNoneIdx = i
        return currNodeIdx
        
    @staticmethod
    def popBestNodeOfList(nlist:list[PathNode]) -> PathNode:
        idx = Pathfinder.findBestNode(nlist)
        return nlist.pop(idx)
    
    
