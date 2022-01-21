from cmath import inf
from pyd2bot import Constants
from pyd2bot.logic.common.frames.DisconnectionHandlerFrame import DisconnectionHandlerFrame
from pyd2bot.logic.common.managers.playerManager import PlayerManager
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
from pyd2bot.misc.interClient.interClientManager import InterClientManager
from pyd2bot.misc.interClient.storeDataManager import StoreDataManager


class rolePlayMovementFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        