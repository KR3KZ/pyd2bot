import threading
from pyd2bot.gameData.world.map import Map
from pyd2bot.utils.pathFinding import Pathfinding
import pyd2bot.network.connection as conn

class IBot:
    
    def __init__(self) -> None:
        self._login = None
        self._password = None
        self.name = None
        self.serverID = None
        
        self.accountId = None
        self.communityId = None
        self.hasRights = None
        self.hasConsoleRight = None
        self.nickname = None
        self.tag = None
        self.subscriptionEndDate = None
        self.subscriptionDurationElapsed = None
        self.secretQuestion = None
        self.accountCreation = None
        self.wasAlreadyConnected = None
        self.characterID = None
        self.inventoryWeight = None
        self.weightMax = None
        
        self.farming = threading.Event()
        self.farmingError = threading.Event()
        self.mapDataReceived = threading.Event()
        self.moving = threading.Event()
        self.idle = threading.Event()
        self.disconnected = threading.Event()
        self.inGame = threading.Event()
        self.onMap = threading.Event()
        self.inServerSelection = threading.Event()
        self.connected = threading.Event()
        
        self.currCellId:int = None
        self.direction:int = None
        self.currMap:Map = None
        self.currMapId:int = None
        self.currFarmingElem:int = None
        self.currMapInteractiveElems:dict = {}
        self.currMapStatedElems:dict = {}
        self.pf = Pathfinding()
        self.conn = conn.Connection(self)