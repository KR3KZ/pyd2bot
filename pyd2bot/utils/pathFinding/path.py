import math
from com.ankamagames.atouin.data.map.map import Map

class Direction:
    direction:int
    outgoingCellId:int
    
    def __init__(self, direction:int, outgoingCellId:int):
        self.direction = direction
        self.outgoingCellId = outgoingCellId
class PathNode:
    
    def __init__(self, id:int, incomingDirection:int, parent:'PathNode'):
        self.id = id
        self.parent = parent
        self.incomingDirection = incomingDirection
        self.outGoingDirection = -1
        self.isAccessible:bool = None
        self.x:float = None
        self.y:float = None
        self.g:float = 0 # distance [noeud courant / parent]
        self.f:float = 0 # distance [noeud courant / parent] + [noeud courant / noeud cible]
        self.h:float = 0 # distance [noeud courant / cible]
        self.cost:int = 0  # nombre de noeuds traversés
        self.destNode:PathNode = None
        self.outgoingCellId:int = None # uniquement pour les MapNodes
        
    def setHeuristic(self, destNode:'PathNode') -> None: 
        if self.parent: 
            self.g = self.parent.g + self.distanceTo(self.parent)
            self.cost = self.parent.cost + 1
        
        else:
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
    
    def __hash__(self) -> int:
        return self.id

class Path(list[PathNode]):
    
    def __init__(self, name:str="anonymous", isLoop:bool=False, nodes:list[PathNode]=list[PathNode](), currentPos:int=0):
        super().__init__(nodes)
        self.name = name
        self.currentPos = currentPos
        self.isLoop = isLoop
    
    def nextDirection(self) -> Direction: 
        if self.isLoop and self.currentPos == len(self): # absolument inutile car il ne rend pas la main
            self.currentPos = 0
        elif self.currentPos == len(self) - 1: # on ne s'intéresse pas au noeud d'arrivée
            return None
        currentNode = self[self.currentPos]
        self.currentPos += 1
        return Direction(currentNode.outGoingDirection, currentNode.outgoingCellId)
    
    def getFirstNode(self) -> PathNode: 
        return self[0]
    
    def getLastNode(self) -> PathNode: 
        return self[-1]
    
    def resetPosition(self) -> None: 
        self.currentPos = 0
    
    def getCrossingDuration(self) -> int: 
        pathLen = len(self)
        time = 0
        for pn in self: # on saute la première cellule
            if pathLen > 3:
                time += pn.getCrossingDuration(True) # courir
            else:
                time += pn.getCrossingDuration(False) # marcher
        return time
    
    def getIdsList(self) -> list[int]: 
        return [node.id for node in self]
    
    def __str__(self) -> str: 
        res = "Path \"" + self.name + "\" : \n"
        for node in self:
            res += str(node) + "\n"
        return res

    def addNode(self, id:int, direction:int) -> None: 
        if direction != Map.LEFT and direction != Map.RIGHT and direction != Map.UP and direction != Map.DOWN:
            raise Exception("Invalid direction for create a node path.")
        self.append(SimplePathNode(id, direction))

class SimplePathNode(PathNode):  # pour les paths enregistrés dans le fichier "paths.txt"

    def __init__(self, id:int, direction:int):
        super().__init__(id, incomingDirection=-1, parent=None)
        self.direction = direction

    def getCrossingDuration(self, mode:bool) -> int: 
        raise Exception("Phony method !")
    
    def setNode(self) -> None: 
        pass
    
    def __str__(self) -> str: 
        return str(self.id)
