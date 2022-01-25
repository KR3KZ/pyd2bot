from pyd2bot.utils.pathFinding.path import Path, PathNode
import logging
logger = logging.getLogger("bot")


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
    
    def getNeighbours(self, node:PathNode) -> dict[int, PathNode]:
        pass
    
    def compute(self, srcId:int, destId:int) -> Path:
        logger.debug("Computing path from " + str(srcId) + " to " + str(destId))
        currNode = self.getNodeFromId(srcId)
        if currNode is None or not currNode.isAccessible:
            logger.error(f"Invalid source node of id {srcId} because accessible={currNode.isAccessible}.")
            return None
        destNode = self.getNodeFromId(destId)
        if destNode is None or not destNode.isAccessible:
            logger.error("Invalid destination node of id " + str(destId) + " because accessible=" + str(destNode.isAccessible))
            return None
        opened = dict[int, PathNode]()
        closed = dict[int, PathNode]()
        while currNode != destNode:
            neighbours = self.getNeighbours(currNode)
            logger.debug("Neighbours of " + str(currNode.id) + ": " + str(neighbours.keys()))
            for nid, neighbor in neighbours.items():
                neighbor.setHeuristic(destNode)
                logger.debug(f"Neighbour {neighbor.id} of {currNode.id} has heuristic {neighbor.f}")
                if neighbor.isAccessible:
                    logger.debug(f"Neighbour {neighbor.id} of {currNode.id} is accessible")
                    if nid in closed:
                        continue	
                    elif nid not in opened or neighbor.g < opened[nid].g:
                        opened[nid] = neighbor
            closed[currNode.id] = currNode
            currNode = self.getBestCandidate(opened)
            if currNode is None: 
                return None
        path = Path()
        direction = -2
        while currNode: 
            if direction != -2:
                currNode.outGoingDirection = direction
            currNode.setNode()
            direction = currNode.incomingDirection
            path.insert(0, currNode)
            currNode = currNode.parent
        logger.debug("found path: " + str(path))
        return path
    
    @staticmethod
    def getBestCandidate(nset:dict[int, PathNode]):
        if not nset:
            return None
        besti = 0
        bestf = float('inf')
        for i, node in nset.items():
            if node.f < bestf:
                bestf = node.f
                besti = i
        return nset.pop(besti)