from http import server
import threading

class PlayerManager:
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
    moving = threading.Event()
    idle = threading.Event()
    disconnected = threading.Event()
    inGame = threading.Event()
    onMap = threading.Event()
    inServerSelection = threading.Event()
    connected = threading.Event()
    farming = threading.Event()
    