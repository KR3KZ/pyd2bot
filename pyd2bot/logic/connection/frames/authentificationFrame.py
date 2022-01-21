from cmath import inf
from pyd2bot import Constants
from pyd2bot.logic.common.frames.DisconnectionHandlerFrame import DisconnectionHandlerFrame
from pyd2bot.logic.common.managers.playerManager import PlayerManager
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
from pyd2bot.misc.interClient.interClientManager import InterClientManager
from pyd2bot.misc.interClient.storeDataManager import StoreDataManager


class AuthentificationFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "ServerConnectionFailedMessage":
            self.client.closeConnection()
            if self.client.login_attempts < Constants.MAX_LOGIN_ATTEMPTS:
                self.client.connectToLoginServer()
            else:
                self.client.killSig.set()
                return True
            return True 
       
        if mtype == "HelloConnectMessage":
            AuthentificationManager.setSalt(msg["salt"])
            AuthentificationManager.setPublicKey(msg["key"])
            AuthentificationManager.initAESKey()
            iMsg = AuthentificationManager.getIdentificationMessage(self.client._login, self.client._password)
            #_log.info("Current version : " + iMsg.version.major + "." + iMsg.version.minor + "." + iMsg.version.code + "." + iMsg.version.build)
            self.client.send(iMsg)
            if InterClientManager.flashKey:
                flashKeyMsg = {'__type__': 'ClientKeyMessage', 'key': InterClientManager.flashKey}
                self.client.send(flashKeyMsg)
            return True
        
        if mtype == "IdentificationSuccessMessage":
            if msg["login"]:
                AuthentificationManager.username = msg["login"]
            PlayerManager.accountId = msg["accountId"]
            PlayerManager.communityId = msg["communityId"]
            PlayerManager.hasRights = msg["hasRights"]
            PlayerManager.hasConsoleRight = msg["hasConsoleRight"]
            PlayerManager.nickname = msg["accountTag"]["nickname"]
            PlayerManager.tag = msg["accountTag"]["tagNumber"]
            PlayerManager.subscriptionEndDate = msg["subscriptionEndDate"]
            PlayerManager.subscriptionDurationElapsed = msg["subscriptionElapsedDuration"]
            PlayerManager.secretQuestion = msg["secretQuestion"]
            PlayerManager.accountCreation = msg["accountCreation"]
            PlayerManager.wasAlreadyConnected = msg["wasAlreadyConnected"]
            # if(msg.wasAlreadyConnected):
            #     KernelEventsManager.processCallback(HookList.AlreadyConnected)
            return True
        
        if mtype == "IdentificationFailedForBadVersionMessage":
            self.client.closeConnection()
            return True
        
        if mtype == "IdentificationFailedBannedMessage":
            self.client.closeConnection()
            return True
        
        if mtype == "IdentificationFailedMessage":
            self.client.closeConnection()
            return True
        
        else:
            return False


