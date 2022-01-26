
from pyd2bot.logic.frames import IFrame
import logging
logger = logging.getLogger("bot")


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
            if int(msg["characterId"]) == self.id:
                self.bot.isReady.set()

        elif mtype == "GameEntitiesDispositionMessage":
            for disposition in msg["dispositions"]:
                cellId = disposition["cellId"]
                if int(disposition["id"]) == self.bot.characterId:
                    self.bot.currCellId = cellId
                else:
                    self.bot.mobsDispositions.append(cellId)
            return True
        
        elif mtype == "GameFightShowFighterMessage":
            return True