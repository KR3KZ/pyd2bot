import logging
import random
from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.logic.common.managers.mapManager import MapManager
logger = logging.getLogger("bot")
import pyd2bot.clientMain as conn
from pyd2bot.utils.pathFinding import Pathfinding
from . import IBot

class Bot(conn.DofusClient, IBot):

    def __init__(self):
        super(Bot, self).__init__()
        self.pf = Pathfinding()
        self.context = 1
        
    def harvest(self):
        pass
    
    def gameContextCreate(self) :
        self.send({'__type__': 'GameContextCreateRequestMessage'})
        
    def requestMapData(self):
        self.send({
            '__type__': 'MapInformationsRequestMessage', 
            'mapId': int(Bot.currMapId)
        })

    def walkToCell(self, cellId):
        print("current bot cellId: " + str(self.currCellId))
        print("current bot mapId: " + str(self.currMapId))
        hash = bytes(random.getrandbits(8) for _ in range(48))
        self.pf.updatePosition(Bot.currMap, Bot.currCellId)
        self.send(
        {
            '__type__': 'GameMapMovementRequestMessage',
            'hash_function': hash,
            'keyMovements': self.pf.getCellsPathTo(cellId),
            'mapId': Bot.currMapId
        })
            
            