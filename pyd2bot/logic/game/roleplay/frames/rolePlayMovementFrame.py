from pyd2bot.logic.common.managers.playerManager import PlayerManager
from pyd2bot.logic.common.managers.mapManager import MapManager
import pyd2bot.world.dofus as dofus
import logging

logger = logging.getLogger("bot")


class RolePlayMovementFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "MapComplementaryInformationsDataMessage":
            MapManager.currMapInteractiveElems  = {}
            MapManager.currMapStatedElems = {}
            
            for ielem in msg["interactiveElements"]:
                MapManager.currMapInteractiveElems[ielem["elementId"]] = ielem
            
            for selem in msg["statedElements"]:
                MapManager.currMapStatedElems[selem["elementId"]] = selem
            return True
                
        elif mtype == "CurrentMapMessage":
            MapManager.currMapId = msg["mapId"]
            MapManager.currPos = MapManager.getMapCoords(MapManager.currMapId)
            PlayerManager.onMap.set()
            return True
            
        elif mtype == "GameMapMovementRequestMessage":
            PlayerManager.moving.set()
            PlayerManager.idle.clear()
            return True
            
        elif mtype == "GameMapMovementConfirmMessage":
            PlayerManager.moving.clear()
            PlayerManager.idle.set()
            return True
                    
        elif mtype == "ChatClientMultiMessage":
            pass