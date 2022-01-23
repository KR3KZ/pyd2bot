from webbrowser import open_new
from pyd2bot.utils.pathFinding.path import Path, PathNode


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
    
    def getNeighbourNodes(self, node:PathNode) -> dict[int, PathNode]:
        pass
    
    def compute(self, srcId:int, destId:int) -> Path:
        print("computing path from " + str(srcId) + " to " + str(destId))
        currentNode = self.getNodeFromId(srcId)
        if currentNode is None:
            raise Exception("Invalid current node id.")
        self.destNode = self.getNodeFromId(destId)
        if self.destNode is None:
            raise Exception("Invalid destination node id.")
        openedList = list[PathNode]()
        closedList = list[PathNode]()
        
        while currentNode != self.destNode:
            print("*************************************************************************")
            print("current node: " + str(currentNode.id))
            neighbours = self.getNeighbourNodes(currentNode)
            print("current node neighbours: " + str(neighbours.keys()))
            for neighbourNode in neighbours.values(): 
                if neighbourNode.isAccessible: # skip obstacles
                    print("found accessible neighbour: " + str(neighbourNode.id))
                    idx, node = self.nodeIsInList(neighbourNode, closedList)
                    if node: # already visited all its neighbours
                        continue	
                    print("neighbour node not in closed list")
                    idx, node = self.nodeIsInList(neighbourNode, openedList)
                    if node:  # already visited
                        print("neighbour node in opened list at index " + str(idx))
                        if neighbourNode.g < node.g:
                            openedList[idx] = neighbourNode # update distance
                    else:
                        print("neighbour first visit")
                        openedList.append(neighbourNode)
            print("opened list size: " + str(len(openedList)))
            closedList.append(currentNode)
            currentNode = self.popBestNodeOfList(openedList)
            print("poped node from opened: " + str(currentNode))
            if currentNode is None: # no path found
                return None
            
        if currentNode == self.destNode:
            print("found destination node " + str(self.destNode.id))
        
        path = Path()
        direction = -2
        while currentNode: 
            if direction != -2: # -2 corresponds to the destination node
                currentNode.outGoingDirection = direction
            currentNode.setNode() # finds the outgoing cell (only for MapNodes)
            direction = currentNode.incomingDirection
            path.insert(0, currentNode)
            currentNode = currentNode.parent
        print("resulting path: " + str(path))
        return path
    
    @staticmethod
    def findBestNode(nlist:list[PathNode]):
        if len(nlist) == 0:
            return None
        currNodeIdx = 0
        for i, listNode in enumerate(nlist):
            print("node f = " + str(listNode.f))
            if listNode.f < nlist[currNodeIdx].f:
                currNodeIdx = i
        return currNodeIdx
        
    @staticmethod
    def popBestNodeOfList(nlist:list[PathNode]) -> PathNode:
        idx = Pathfinder.findBestNode(nlist)
        print("found best node at index " + str(idx))
        if idx is not None:
            return nlist.pop(idx)
        else:
            return None