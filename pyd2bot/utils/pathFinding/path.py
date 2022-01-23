from pyd2bot.gameData.world.map import Map
from pyd2bot.utils.pathFinding.pathFinder import PathNode
from pyd2bot.utils.pathFinding.pathFinding import Direction


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
    
    def __str__(self, ) -> str: 
        str = "Path \"" + self.name + "\" : \n"
        for node in self:
            str += node + "\n"
        return str

    def addNode(self, id:int, direction:int) -> None: 
        if direction != Map.LEFT and direction != Map.RIGHT and direction != Map.UP and direction != Map.DOWN:
            raise Exception("Invalid direction for create a node path.")
        self.append(SimplePathNode(id, direction))
    
    def reverse(self) -> None: 
        self.reverse()


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
    
    
