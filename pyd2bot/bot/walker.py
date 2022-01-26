from time import sleep
import logging
import random
from .bot import Bot
logger = logging.getLogger("bot")


class Walker(Bot):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def walkToCell(self, cellId):
        self.inGame.wait()
        logger.info(f"Current cellId: {self.currCellId}")
        logger.debug(f"Current mapId: {self.currMapId}")
        if self.currCellId == cellId:
            logger.info(f"Already in cell {cellId}")
            return True
        self.pf.updatePosition(self.currMap, self.currCellId)
        keymoves = self.pf.getCellsPathTo(cellId)
        if keymoves:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            self.moving.clear()
            self.moveError.clear()
            self.conn.send({
                '__type__': 'GameMapMovementRequestMessage',
                'hash_function': hash,
                'keyMovements': keymoves,
                'mapId': self.currMapId
            })
            logger.info(f"Walk request to cell {cellId} sent")
            if self.moving.wait():
                if self.moveError.is_set():
                    logger.error("Moving error")
                    return False
                else:
                    sleep(self.pf.getCellsPathDuration())
                    self.conn.send({'__type__': "GameMapMovementConfirmMessage"})
                    self.currCellId = cellId
                    logger.info(f"Moved to cell {self.currCellId}")
                    return True
            else:
                logger.error(f"Failed to walk to cell {cellId}")
                return False
        else:
            logger.error(f"No path to cellId {cellId} found")
            return False

    
    def randWalk(self):
        currMapZone = self.currMap.zones.getZone(self.currCellId)
        logger.info(f"Current map zone has possible directions {currMapZone.getPossibleMapChangeDirections()}")
        direction, cellId = currMapZone.getRandMapChange()
        logger.info(f"Picked rand direction {direction} from cell {cellId}")
        dstMapId = self.currMap.getNeighborIdFromDirection(direction)
        logger.info(f"Going to map {dstMapId}")
        if self.walkToCell(cellId):
            self.mapDataLoaded.clear()
            self.mapComplementaryInfosReceived.clear()
            self.conn.send({
                '__type__': 'ChangeMapMessage', 
                'autopilot': False, 
                'mapId': dstMapId
            })
            if self.mapDataLoaded.wait(timeout=5):
                logger.info(f"Entered to map {dstMapId}")
                if self.mapComplementaryInfosReceived.wait():
                    self.mapDataLoaded.clear()
                    self.mapComplementaryInfosReceived.clear()
                    return dstMapId
        logger.error(f"Failed to walk to map {dstMapId}")
        return None
