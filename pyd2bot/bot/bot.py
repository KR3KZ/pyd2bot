import logging
import random
from sys import exc_info
from time import sleep
from . import IBot


logger = logging.getLogger("bot")
class Bot(IBot):

    def __init__(self, name, serverID, login, password) -> None:
        super().__init__()
        self.name = name
        self.serverID = serverID
        self._login = login
        self._password = password

    def disconnect(self):
        self.conn.interrupt()
        
    def login(self):
        self.conn.start()
        self.conn.connectToLoginServer()
        self.mapDataReceived.wait()

    def walkToCell(self, cellId):
        try:
            logger.info("current bot cellId: " + str(self.currCellId))
            logger.info("current bot mapId: " + str(self.currMapId))
            hash = bytes(random.getrandbits(8) for _ in range(48))
            self.pf.updatePosition(self.currMap, self.currCellId)
            keymoves = self.pf.getCellsPathTo(cellId)
            if keymoves:
                self.conn.send(
                {
                    '__type__': 'GameMapMovementRequestMessage',
                    'hash_function': hash,
                    'keyMovements': keymoves,
                    'mapId': self.currMapId
                })
                if self.conn.waitMsg(msgName="GameMapMovementMessage", filter=lambda m: int(m["actorId"]) == self.characterID, timeout=10):
                    sleep(self.pf.getCellsPathDuration())
                    self.conn.send({'__type__': "GameMapMovementConfirmMessage"})
                    self.currCellId = cellId
                    logger.info("bot moved to cellId: " + str(self.currCellId))
                    return True
                else:
                    logger.error("Bot failed to walk to cellId: " + str(cellId))
                    return False
        except Exception as e:
            logger.error("fatal error: ", exc_info=True)
            return False
                
            