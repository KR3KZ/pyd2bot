from pyd2bot.logic.frames import IFrame
import logging
logger = logging.getLogger("bot")


class RolePlayInteractiveFrame(IFrame):

    def __init__(self, bot):
        super().__init__(bot)
        self.botCellID = None
        self.mobsDispositions = []

    def process(self, mtype, msg) -> bool:
        if mtype == "GameFightStartingMessage":
            self.id = msg["attackerId"]
            self.bot.isInFight.set()
        
        elif mtype == "GameEntitiesDispositionMessage":
            for disposition in msg["dispositions"]:
                cellId = disposition["cellId"]
                if disposition["id"] == self.id:
                    self.botCellID = cellId
                else:
                    self.mobsDispositions.append(cellId)
        
        elif mtype == "GameFightShowFighterMessage":
            pass
        
        elif mtype == "GameFightEndMessage":
            self.bot.isInFight.clear()
        
        elif mtype == "GameFightTurnStartPlayingMessage":
            logger.info("Bot turn started")
            self.bot.inFightTurn.set()
        
        elif mtype == "GameFightTurnFinishMessage":
            logger.info("Bot turn ended")
        
        elif mtype == "GameFightJoinMessage":
            if msg["canSayReady"]:
                logger.info("can say ready event set")

        elif mtype == "GameFightReadyMessage":
            if msg["isReady"]:
                logger.info("Game Fight Ready")
        
        elif mtype == "GameActionFightCastRequestMessage":
            logger.info("Spell casted")
                    
        elif mtype == "SequenceStartMessage":
            if msg["authorId"] == self.id and msg["sequenceType"] == 1:
                pass
                
        elif mtype == "SequenceEndMessage":
            if msg["authorId"] == self.id and msg["sequenceType"] == 1:
                pass
            
        elif mtype == "RefreshCharacterStatsMessage":
            if msg["fighterId"] == self.id:
                for characteristic in msg["stats"]["characteristics"]["characteristics"]:
                    value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                            characteristic["objectsAndMountBonus"]
                    if characteristic["characteristicId"] == 23:
                        self.pm = value - characteristic["used"]
                    elif characteristic["characteristicId"] == 1:
                        self.pa = value - characteristic["used"]
                logger.info(f"Bot pa, pm: {self.pa, self.pm}")

        elif mtype == "GameFightSynchronizeMessage":
            self.monsters = []
            for fighter in msg["fighters"]:
                if fighter["__type__"] == "GameFightCharacterInformations" and fighter["contextualId"] == self.id:
                    self.currCellId = fighter["disposition"]["cellId"]
                    for characteristic in fighter["stats"]["characteristics"]["characteristics"]:
                        value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                            characteristic["objectsAndMountBonus"]
                        if characteristic["characteristicId"] == 23:
                            self.pm = value - characteristic["used"]
                        elif characteristic["characteristicId"] == 1:
                            self.pa = value - characteristic["used"]
                elif fighter["__type__"] == "GameFightMonsterInformations":
                    self.monsters.append(
                        {
                            "cellID": fighter["disposition"]["cellId"],
                            "summoned": fighter["stats"]["summoned"]
                        }
                    )