from pyd2bot.gameData.world.map import Map
from pyd2bot.utils.pathFinding.pathFinder import PathNode
from pyd2bot.utils.pathFinding.pathFinding import Direction


class Path:
    name:str
    nodes:list[PathNode]
    currentPos:int
    isLoop:bool
    startCellId = -1 # uniquement pour les paths de maps
    
    def __init__(self, name:str="anonymous", isLoop:bool=False, nodes:list[PathNode]=list[PathNode](), currentPos:int=0): 
        self.name = name
        self.nodes = nodes
        self.currentPos = currentPos
        self.isLoop = isLoop
    
    def nextDirection(self) -> Direction: 
        if(self.isLoop and self.currentPos == self.nodes.size()): # absolument inutile car il ne rend pas la main
            self.currentPos = 0
        elif self.currentPos == len(self.nodes) - 1: # on ne s'intéresse pas au noeud d'arrivée
            return None
        currentNode = self.nodes[self.currentPos]
        self.currentPos += 1
        return Direction(currentNode.direction, currentNode.outgoingCellId)
    
    def getName(self) -> str: 
        return self.name
    
    def getFirstNode(self) -> PathNode: 
        return self.nodes[0]
    
    def getLastNode(self) -> PathNode: 
        return self.nodes[-1]
    
    def resetPosition(self) -> None: 
        self.currentPos = 0
    
    def getCrossingDuration(self) -> int: 
        pathLen = len(self.nodes)
        time = 0
        for i in range(pathLen): # on saute la première cellule
            if pathLen > 3:
                time += self.nodes[i].getCrossingDuration(True) # courir
            else:
                time += self.nodes[i].getCrossingDuration(False) # marcher
        return time
    
    def toVector(self) -> list[int]: 
        vector = list[int]()
        for node in self.nodes:
            vector.append(node.id)
        return vector
    
    def __str__(self, ) -> str: 
        str = "Path \"" + self.name + "\" : \n"
        for node in self.nodes:
            str += node + "\n"
        return str

    def addNode(self, id:int, direction:int) -> None: 
        if direction != Map.LEFT and direction != Map.RIGHT and direction != Map.UP and direction != Map.DOWN:
            raise Exception("Invalid direction for create a node path.")
        self.nodes.append(SimplePathNode(id, direction))
    
    def addNode(self, node:PathNode) -> None: 
        self.nodes.append(node)
    
    def reverse(self) -> None: 
        self.nodes.reverse()


class SimplePathNode(PathNode):  # pour les paths enregistrés dans le fichier "paths.txt"

    def __init__(self, id:int, direction:int):
        super().__init__(id, -1, None)
        self.direction = direction
    

    def getCrossingDuration(self, mode:bool) -> int: 
        raise Exception("Phony method !")
    
    def setNode(self, ) -> None: 
        pass
    
    def __str__(self) -> str: 
        return str(self.id)
    
    
