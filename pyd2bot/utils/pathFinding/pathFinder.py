

import math


class PathNode:
    id:int
    x:float
    y:float
    parent:'PathNode'
    g:float # distance [noeud courant / parent]
    f:float # distance [noeud courant / parent] + [noeud courant / noeud cible]
    h:float # distance [noeud courant / cible]
    cost:int # nombre de noeuds traversés
    isAccessible:bool
    lastDirection:int
    direction:int
    outgoingCellId:int # uniquement pour les MapNodes
    
    def __init__(self, id:int, lastDirection:int, parent:'PathNode'):
        self.id = id
        self.parent = parent
        self.lastDirection = lastDirection
        self.direction = -1
    
    def setHeuristic(self, destNode:'PathNode') -> None: 
        if self.parent is not None: 
            self.g = self.parent.g + self.distanceTo(self.parent)
            self.cost = self.parent.cost + 1
        
        else:  # noeud initial et noeud final
            self.g = 0
            self.cost = 0
        
        if destNode is not None: 
            self.h = self.distanceTo(destNode)
            self.f = self.g + self.h
    
    def distanceTo(self, node:'PathNode') -> float: 
        return math.sqrt(math.pow(node.x - self.x, 2) + math.pow(node.y - self.y, 2))
    
    def __eq__(self, node:'PathNode') -> bool: 
        return self.id == node.id
    
    def setNode(self) -> None:
        pass
    
    def getCrossingDuration(mode:bool) -> int:
        pass
    
    def __str__(self):
        pass


class Pathfinder:
    
    currentNode:PathNode
    destNode:PathNode
    path:Path
    openedList:list[PathNode]
    closedList:list[PathNode]
    
    def getNodeFromId(id:int) -> PathNode:
        pass
    
    def nodeIsInList(node:PathNode, list:list[PathNode]) -> PathNode:
        pass
    
    def getNeighbourNodes(node:PathNode) -> list[PathNode]:
        pass
    
    @staticmethod
    def compute(srcId:int, destId:int) -> Path: 
        currentNode = Pathfinder.getNodeFromId(srcId)
        if currentNode == None:
            raise Exception("Invalid current node id.")
        destNode = Pathfinder.getNodeFromId(destId)
        if destNode == None:
            raise Exception("Invalid destination node id.")
        openedList = list[PathNode]()
        closedList = list[PathNode]()
        
        while not currentNode == destNode: 
            neighbours = Pathfinder.getNeighbourNodes(currentNode)
            for neighbourNode in neighbours: 
                if not neighbourNode.isAccessible: # obstacle
                    continue
                if Pathfinder.nodeIsInList(neighbourNode, closedList) is not None: # déjà traitée
                    continue	
                inListNode = Pathfinder.nodeIsInList(neighbourNode, openedList)
                if inListNode is not None:  # déjà une possibilité
                    if neighbourNode.g < inListNode.g:
                        inListNode = neighbourNode # modification de la référence dans la liste
                else:
                    openedList.append(neighbourNode)	
            
            closedList.append(currentNode)
            currentNode = Pathfinder.popBestNodeOfList(openedList)
            if currentNode == None: # pas de chemin possible
                return None
        
        path = Path()
        direction = -2
        while currentNode is not None: 
            if direction != -2: # -2 correspond au noeud d'arrivée
                currentNode.direction = direction # on fixe la direction du noeud grâce à la propriété "lastDirection" du noeud fils
            currentNode.setNode() # on fixe la cellule du sortie du noeud (pour:uniquement les chemins de maps)
            direction = currentNode.lastDirection
            path.append(currentNode)
            currentNode = currentNode.parent
        
        path.reverse()
        return path
    
    @staticmethod
    def popBestNodeOfList(nlist:list[PathNode]) -> PathNode: 
        if len(nlist) == 0:
            return None
        currentNode = nlist[0]
        for listNode in nlist: 
            if listNode.f < currentNode.f:
                currentNode = listNode
        del currentNode
        return currentNode
    
    
