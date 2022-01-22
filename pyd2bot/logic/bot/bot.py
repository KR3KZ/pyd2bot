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

    def walkToCell(self):
        self.send(
        {
            '__type__': 'GameMapMovementRequestMessage',
            'hash_function': bytearray(b'\xeb\x9a%^\x9b\xc2\xe4!\xe9($\x1c,\xdb\xc5\x12'
                                        b"\xd8\xad\xa4\xba5a \xac\x84\x853\x0bJ'\xe43"
                                        b"'J\x92\xb8\x03\xb6}\xaf\x84\x99\xbd1\x18\xb0\x7fL"),
            'keyMovements': [4520, 4534],
            'mapId': 193331716.0
        })
            
            