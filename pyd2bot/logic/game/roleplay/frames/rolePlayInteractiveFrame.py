from cmath import inf
from pyd2bot import Constants
from pyd2bot.logic.common.frames.DisconnectionHandlerFrame import DisconnectionHandlerFrame
from pyd2bot.logic.common.managers.mapManager import MapManager
from pyd2bot.logic.common.managers.playerManager import PlayerManager
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
from pyd2bot.misc.interClient.interClientManager import InterClientManager
from pyd2bot.misc.interClient.storeDataManager import StoreDataManager
import logging

logger = logging.getLogger("bot")


class RolePlayInteractiveFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "InteractiveUseErrorMessage":
            self.farmingError.set()
            return True
        
        elif mtype == "InteractiveUsedMessage":
            skill = msg["skillId"]
            self.currFarmingElem = msg["elemId"]
            logger.info(f"Farming animation of elem {self.currFarmingElem} with skill {skill} started")
            PlayerManager.farming.set()
            return True
        
        elif mtype == "InteractiveUseEndedMessage":
            logger.info(f"Farming animation of elem {self.currFarmingElem} ended")
            return True
    
        elif mtype == "StatedElementUpdatedMessage":
            elem_id = msg["statedElement"]["elementId"]
            MapManager.currMapStatedElems[elem_id] = msg["statedElement"]
            logger.info(f"Element {elem_id} state changed")
            return True
        
        elif mtype == "InteractiveElementUpdatedMessage":
            elem_id = msg["interactiveElement"]["elementId"]
            MapManager.currMapInteractiveElems[elem_id] = msg["interactiveElement"]
            logger.info(f"Element {elem_id} interactiveness changed")
            if self.currFarmingElem == elem_id:
                self.currFarmingElem = None
                PlayerManager.farming.clear()
            return True