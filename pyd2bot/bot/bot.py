import logging
import random
from time import sleep

from pyd2bot.utils.pathFinding.cellsPathFinder import CellNode, CellsPathfinder
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
        logger.info("Loging in...")
        self.conn.start()
        self.conn.connectToLoginServer()
        self.mapDataReceived.wait()
        logger.info("Logged in.")

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
            else:
                logger.info("Not path to cellId {0} found".format(cellId))
        except Exception as e:
            logger.error("fatal error: ", exc_info=True)
            return False

    def canCollect(self, elem_id):
        ielem = self.currMapInteractiveElems[elem_id]
        selem = self.currMapStatedElems[elem_id]
        logger.info(f"checking if elem {ielem} can be collected")
        if ielem["onCurrentMap"] and selem["elementState"] == 0 and ielem["enabledSkills"]:
            return ielem["enabledSkills"][0]
        return None     

    def collect(self):
        cpf = CellsPathfinder(self.currMap)
        logger.info("looking for collectable resources")
        for elId in self.currMapInteractiveElems.keys():
            enabledSkill = self.canCollect(elId)         
            if enabledSkill is not None:
                selem = self.currMapStatedElems[elId]
                cell_id = selem["elementCellId"]
                logger.info(f"Collecting elem {elId} in cell {cell_id}")
                cellNode = cpf.getNodeFromId(cell_id)
                neighbors:dict[int, CellNode] = cpf.getNeighbours(cellNode)
                for neighbor in neighbors.values():
                    if neighbor.isAccessible:
                        if self.walkToCell(neighbor.id):
                            hash = bytes(random.getrandbits(8) for _ in range(48))
                            self.conn.send({
                                '__type__': 'InteractiveUseRequestMessage',
                                'elemId': elId,
                                'hash_function': hash,
                                'skillInstanceUid': enabledSkill["skillInstanceUid"],
                            })
                            if self.farming.wait(20):
                                logger.info(f"Collecting elem {elId}")
                                while self.farming.is_set():
                                    sleep(0.01)
                                logger.info(f"Collected elem {elId}")
                                break
                            else:
                                logger.error("farming failed")
                            

                        
                    