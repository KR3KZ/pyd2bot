import threading
from pyd2bot.gameData.world.map import Map
from pyd2bot.utils.pathFinding import Pathfinding
import pyd2bot.network.connection as conn
from pyd2bot.utils.pathFinding.cellsPathFinder import CellsPathfinder

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
        

        self.farmingError = threading.Event()
        self.inGame = threading.Event()
        
        self.isInFight = threading.Event()
        self.inFightTurn = threading.Event()
        self.fightCurrCellId = None
        self.currCellId:int = None
        self.direction:int = None
        self.currMap:Map = None
        self.currMapId:int = None
        self.currFarmingElem:int = None
        self.currMapInteractiveElems:dict = {}
        self.currMapStatedElems:dict = {}
        self.pf = Pathfinding()
        self.cpf = CellsPathfinder()
        self.conn = conn.Connection(self)
        self._kill = self.conn._kill