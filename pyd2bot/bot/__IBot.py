import threading
from pyd2bot.gameData.world.map import Map


class IBot:
    accountId = None
    communityId = None
    hasRights = None
    hasConsoleRight = None
    nickname = None
    tag = None
    subscriptionEndDate = None
    subscriptionDurationElapsed = None
    secretQuestion = None
    accountCreation = None
    wasAlreadyConnected = None
    characterID = None
    characterName = None
    serverID = None
    inventoryWeight = None
    weightMax = None
    
    farming = threading.Event()
    farmingError = threading.Event()
    mapDataReceived = threading.Event()
    moving = threading.Event()
    idle = threading.Event()
    disconnected = threading.Event()
    inGame = threading.Event()
    onMap = threading.Event()
    inServerSelection = threading.Event()
    connected = threading.Event()
    
    currCellId:int = None
    direction:int = None
    currMap:Map = None
    currMapId:int = None
    currMapInteractiveElems:dict = {}
    currMapStatedElems:dict = {}
    
    