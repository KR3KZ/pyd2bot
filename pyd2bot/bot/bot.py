import logging
import random
from time import sleep
from pyd2bot.utils.pathFinding.MapsPathFinder import MapNode
from pyd2bot.utils.pathFinding.path import Path
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
        if self.conn.waitMsg("IdentificationSuccessMessage"):
            logger.info("Identified successfully")
            if self.conn.waitMsg("TrustStatusMessage"):
                logger.info("Logged to game server successfully.")
                if self.conn.waitMsg("CharacterLoadingCompleteMessage"):
                    logger.info("Characted loading completed.")
                    if self.conn.waitMsg("MapComplementaryInformationsDataMessage"):
                        logger.info("Map complementary Data Recieved.")
                        return True
        return False


    def walkToCell(self, cellId):
        logger.debug(f"Current cellId: {self.currCellId}")
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
            if self.conn.waitMsg("GameMapMovementMessage", filter=lambda m: int(m["actorId"]) == self.characterID):
                sleep(self.pf.getCellsPathDuration())
                self.conn.send({'__type__': "GameMapMovementConfirmMessage"})
                self.currCellId = cellId
                logger.info(f"bot moved to cell {self.currCellId}")
                return True
            else:
                logger.error(f"Failed to walk to cell {cellId}")
                return False
        else:
            logger.error(f"No path to cellId {cellId} found")
            return False


    def canCollect(self, elem_id):
        logger.debug(f"Checking if elem {elem_id} can be collected")
        if elem_id in self.currMapStatedElems:
            ielem = self.currMapInteractiveElems[elem_id]
            selem = self.currMapStatedElems[elem_id]
            if ielem["onCurrentMap"] and selem["elementState"] == 0 and ielem["enabledSkills"]:
                return ielem["enabledSkills"][0]
        return None     


    def collectElement(self, elementId, skill):
        selem = self.currMapStatedElems[elementId]
        cellId = selem["elementCellId"]
        cellNode = self.cpf.getNodeFromId(cellId)
        neighbors = self.cpf.getAccessibleNeighbours(cellNode)
        for ncid in neighbors:
            if self.walkToCell(ncid):
                hash = bytes(random.getrandbits(8) for _ in range(48))
                self.conn.send({
                    '__type__': 'InteractiveUseRequestMessage',
                    'elemId': elementId,
                    'hash_function': hash,
                    'skillInstanceUid': skill["skillInstanceUid"],
                })
                if self.conn.waitMsg("InteractiveUsedMessage"):
                    logger.info(f"Collecting elem {elementId} ...")
                    if self.conn.waitMsg("InteractiveUseEndedMessage"):
                        logger.info(f"Element {elementId} collected")
                        break
                if self._kill.is_set():
                    return


    def harvest(self):
        self.cpf.map = self.currMap
        logger.info("Looking for collectable resources")
        for id in self.currMapInteractiveElems.keys():
            enabledSkill = self.canCollect(id)         
            if enabledSkill is not None:
                self.collectElement(id, enabledSkill)
                if self._kill.is_set():
                    return
    
    
    def walkToMap(self, targetMapId):
        path:list[MapNode] = self.pf.toMap(self.currMapId, targetMapId, self.currCellId)
        pathLen = len(path)
        logger.info(f"Path to map {path}")
        for i in range(pathLen - 1):
            if self.walkToCell(path[i].outgoingCellId):
                self.conn.send({
                    '__type__': 'ChangeMapMessage', 
                    'autopilot': False, 
                    'mapId': path[i + 1].id
                })
                if self.conn.waitMsg("CurrentMapMessage", filter=lambda m: int(m["mapId"]) == path[i + 1].id):
                    logger.info(f"Entered to map {path[i + 1].id}")
                else:
                    logger.error(f"Failed to walk to map {path[i + 1].id}")
                    return None



                
                        

                        
                    