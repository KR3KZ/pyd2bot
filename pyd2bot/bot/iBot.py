import threading
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.atouin.data.map.Map import Map
from pyd2bot.logic.managers import EventsManager
from pyd2bot.utils.pathFinding import Pathfinding
from pyd2bot.network import Connection, MsgListner
from pyd2bot.utils.pathFinding.cellsPathFinder import CellsPathfinder
import pyd2bot.logic.frames as msgframes

class IBot:
    
    def __init__(self, name, login, password, serverID):

        # creds data
        self.name = name
        self.serverID = serverID
        self._login = login
        self._password = password
        
        # Account data
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
        self.characterId = None
        self.inventoryWeight = None
        self.weightMax = None
        
        # kill sig
        self._kill = threading.Event()

        # Some game events
        self.farming = threading.Event()
        self.moving = threading.Event()
        self.idle = threading.Event()
        self.moveError = threading.Event()
        self.farmingError = threading.Event()

        # contextual data
        self.contextChanged = threading.Event()
        self.inGame = threading.Event()        
        self.mapDataLoaded = threading.Event()
        self.mapComplementaryInfosReceived = threading.Event()

        # fight data
        self.isInFight = threading.Event()
        self.canSayReady = threading.Event()
        self.isReady = threading.Event()
        self.isTurn = threading.Event()
        self.turnStarted = threading.Event()
        self.turnEnded = threading.Event()
        self.currPA = None
        self.currPM = None
        self.mobsDispositions = []

        # In game data
        self.fightCurrCellId = None
        self.currCellId:int = None
        self.direction:int = None
        self.currMap:Map = None
        self.currMapId:int = None
        self.currFarmingElem:int = None
        self.currMapInteractiveElems:dict = {}
        self.currMapStatedElems:dict = {}

        # Modules
        self.pf = Pathfinding()
        self.cpf = CellsPathfinder()
        self.conn = Connection()
        self.evtMgr = EventsManager()
        frames = [cls_frame(self) for cls_frame in msgframes._cls_frames]
        self.msgListner = MsgListner(self.evtMgr, self.conn, frames)


