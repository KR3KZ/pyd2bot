
from pyd2bot.logic.frames import IFrame
import logging
logger = Logger(__name__)


class FightStartingFrame(IFrame):

    def __init__(self, bot):
        super().__init__(bot)
        self.botCellID = None
        self.mobsDispositions = []

    def process(self, mtype, msg) -> bool:


        if mtype == "GameFightStartingMessage":
            logger.info("GameFightStartingMessage received")
            return True

        elif mtype == "GameFightJoinMessage":
            if msg["canSayReady"]:
                logger.info("can say ready event set")
                self.bot.canSayReady.set()
            return True

        elif mtype == "GameFightHumanReadyStateMessage":
            if int(msg["characterId"]) == self.bot.characterId:
                self.bot.isReady.set()
            return True
        
        elif mtype == "GameFightShowFighterMessage":
            return True