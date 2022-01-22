import logging
from time import sleep

from pyd2bot.logic.common.managers.mapManager import MapManager
logger = logging.getLogger("bot")

import threading
from pyd2bot.network.message import Msg
from pyd2bot.clientMain import DofusClient

class Bot(DofusClient):

    def __init__(self):
        super(Bot, self).__init__()
        self.killsig = threading.Event()
        self.lock = threading.Lock()
        self.fullPods = threading.Event()
        self.fullPodsAAA = threading.Event()
        self.context = 1
            
    def interrupt(self):
        self.killsig.set()
        super().interrupt()
        logger.info('Goodbye cruel world.')

    def harvest(self):
        pass
    
    def gameContextCreate(self) :
        self.send({'__type__': 'GameContextCreateRequestMessage'})
        
    def requestMapData(self):
        self.send({
            '__type__': 'MapInformationsRequestMessage', 
            'mapId': int(MapManager.currMapId)
        })
        
    def handleMsg(self, msg: Msg):
        logger.info("received msg: " + msg.name["name"])     
        if msg.name["name"] == "InventoryWeightMessage":
            msg_json = msg.json()
            self.inventoryWeight = msg_json["inventoryWeight"]
            self.weightMax = msg_json["weightMax"]
            prcnt = self.inventoryWeight / self.weightMax
            if prcnt > 0.9:
                logger.info(f"Bot reached {100 * prcnt} of pod available")
                self.fullPodsAAA.set()
            
        if msg.name["name"] == "NotificationUpdateFlagMessage":
            msg_json = msg.json()
            if msg_json["index"] == 37:
                self.fullPods.set()
                logger.info("Got bot full pod notif from server")
        
        if msg.name["name"] == "GameContextCreateMessage":
            msg_json = msg.json()
            self.context = msg_json["context"]
        
            