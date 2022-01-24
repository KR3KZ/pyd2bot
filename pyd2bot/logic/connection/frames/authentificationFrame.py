import pyd2bot.bot as bot
from pyd2bot import Constants
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.misc.interClient.interClientManager import InterClientManager


class AuthentificationFrame:

    def __init__(self, client):
        self.client = client    
      
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
            self.client.send(iMsg)
            if InterClientManager.flashKey:
                flashKeyMsg = {'__type__': 'ClientKeyMessage', 'key': InterClientManager.flashKey}
                self.client.send(flashKeyMsg)
            return True
        
        if mtype == "IdentificationSuccessMessage":
            if msg["login"]:
                AuthentificationManager.username = msg["login"]
            bot.Bot.accountId = msg["accountId"]
            bot.Bot.communityId = msg["communityId"]
            bot.Bot.hasRights = msg["hasRights"]
            bot.Bot.hasConsoleRight = msg["hasConsoleRight"]
            bot.Bot.nickname = msg["accountTag"]["nickname"]
            bot.Bot.tag = msg["accountTag"]["tagNumber"]
            bot.Bot.subscriptionEndDate = msg["subscriptionEndDate"]
            bot.Bot.subscriptionDurationElapsed = msg["subscriptionElapsedDuration"]
            bot.Bot.secretQuestion = msg["secretQuestion"]
            bot.Bot.accountCreation = msg["accountCreation"]
            bot.Bot.wasAlreadyConnected = msg["wasAlreadyConnected"]

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


