import logging
from . import IBot
logger = logging.getLogger("bot")

class Bot(IBot):

    def __init__(self, name, serverID, login, password) -> None:
        super().__init__(name, login, password, serverID)

    def stop(self):
        self._kill.set()
        self.conn.close()
        self.evtMgr.interrupt()
        self.msgListner.interrupt()
        self.msgListner.join()

    def login(self):
        self.conn.connectToLoginServer()
        self.msgListner.start()
        if self.evtMgr.waitMsg("IdentificationSuccessMessage"):
            logger.info("Identified successfully")
            if self.evtMgr.waitMsg("TrustStatusMessage"):
                logger.info("Logged to game server successfully.")
                if self.evtMgr.waitMsg("CharacterLoadingCompleteMessage"):
                    logger.info("Characted loading completed.")
                    if self.evtMgr.waitMsg("CurrentMapMessage"):
                        logger.info(f"Appeared in map {self.currMapId}.")
                        if self.mapDataLoaded.wait():
                            logger.info("Game Map dlm Ddata loaded.")
                            if self.mapComplementaryInfosReceived.wait():
                                logger.info(f"Map Data Recieved. Bot is on cell {self.currCellId}.")
                                self.mapDataLoaded.clear()
                                return True
        return False





                
                        

                        
                    