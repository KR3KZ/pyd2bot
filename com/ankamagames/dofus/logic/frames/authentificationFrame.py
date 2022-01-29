from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.bot import IBot
from pyd2bot.logic.managers import AuthentificationManager
from pyd2bot.logic.managers.interClientManager import InterClientManager
from com.ankamagames.dofus.network.enums.IdentificationFailureReasonsEnum import IdentificationFailureReasonEnum
from pyd2bot.logic.frames import IFrame
import logging
logger = logging.getLogger("bot")


class AuthentificationFrame(IFrame):
    MAX_LOGIN_ATTEMPTS = 3
    
    def __init__(self, bot:'IBot'):
        super().__init__(bot)
        self._login_attempts = 0
    
    def process(self, mtype, msg) -> bool:
        
        if mtype == "ServerConnectionFailedMessage":
            if self._login_attempts < self.MAX_LOGIN_ATTEMPTS:
                self.conn.connectToLoginServer()
                self._login_attempts += 1
            else:
                self.conn.close()
                return True
            return True 

        elif mtype == "HelloConnectMessage":
            AuthentificationManager.setSalt(msg["salt"])
            AuthentificationManager.setPublicKey(msg["key"])
            AuthentificationManager.initAESKey()
            iMsg = AuthentificationManager.getIdentificationMessage(self.bot._login, self.bot._password)
            self.conn.send(iMsg)
            if InterClientManager.flashKey:
                flashKeyMsg = {
                    '__type__': 'ClientKeyMessage', 
                    'key': InterClientManager.flashKey
                }
                self.conn.send(flashKeyMsg)
            return True
        
        elif mtype == "IdentificationSuccessMessage":
            self.bot.accountId = msg["accountId"]
            self.bot.communityId = msg["communityId"]
            self.bot.hasRights = msg["hasRights"]
            self.bot.hasConsoleRight = msg["hasConsoleRight"]
            self.bot.nickname = msg["accountTag"]["nickname"]
            self.bot.tag = msg["accountTag"]["tagNumber"]
            self.bot.subscriptionEndDate = msg["subscriptionEndDate"]
            self.bot.subscriptionDurationElapsed = msg["subscriptionElapsedDuration"]
            self.bot.secretQuestion = msg["secretQuestion"]
            self.bot.accountCreation = msg["accountCreation"]
            self.bot.wasAlreadyConnected = msg["wasAlreadyConnected"]
            self._done = True
            return True
        
        elif mtype == "IdentificationFailedMessage":
            reason = IdentificationFailureReasonEnum(msg["reason"])
            logger.error("Identification failed for reason: %s" % reason)
            self.conn.interrupt()
            return True
        return False


