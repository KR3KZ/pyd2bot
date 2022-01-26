from time import sleep
import logging
import random
from .bot import Bot
logger = logging.getLogger("bot")


class Walker(Bot):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def walkToCell(self, cellId):
        logger.info(f"Current cellId: {self.currCellId}")
        logger.debug(f"Current mapId: {self.currMapId}")
        if self.currCellId == cellId:
            logger.info(f"Already in cell {cellId}")
            return True
        self.pf.updatePosition(self.currMap, self.currCellId)
        keymoves = self.pf.getCellsPathTo(cellId)
        if keymoves:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            self.conn.send({
                '__type__': 'GameMapMovementRequestMessage',
                'hash_function': hash,
                'keyMovements': keymoves,
                'mapId': self.currMapId
            })
            logger.info(f"Walk request to cell {cellId} sent")
            events = [("GameMapMovementMessage", lambda m: int(m["actorId"]) == self.characterID), ("GameMapNoMovementMessage", None)]
            if self.evtMgr.waitMsgs(events):
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
            self.conn.send({
                '__type__': 'ChangeMapMessage', 
                'autopilot': False, 
                'mapId': dstMapId
            })
            if self.evtMgr.waitMsg("CurrentMapMessage", condition=lambda m: int(m["mapId"]) == dstMapId):
                logger.info(f"Entered to map {dstMapId}")
                if self.mapDataLoaded.wait():
                    logger.info(f"Map {dstMapId} dlm data loaded successfully")
                    self.mapDataLoaded.clear()
                return dstMapId
            else:
                logger.error(f"Failed to walk to map {dstMapId}")
                return None
