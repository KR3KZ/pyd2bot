from pyd2bot.logic.frames import IFrame
import logging
logger = logging.getLogger("bot")


class GameFightFrame(IFrame):

    def __init__(self, bot):
        super().__init__(bot)
        self.botCellID = None
        self.mobsDispositions = []

    def process(self, mtype, msg) -> bool:
        
        if mtype == "GameFightShowFighterMessage":
            return True
        
        elif mtype == "GameFightTurnReadyRequestMessage":
            if int(msg["id"]) == self.bot.characterId:
                self.bot.isFightTurn.set()
                
        elif mtype == "GameFightEndMessage":
            self.bot.isInFight.clear()
            return True

        elif mtype == "GameFightTurnStartPlayingMessage":
            logger.info("Bot turn started")
            self.bot.isFightTurn.set()
            return True
        
        elif mtype == "GameFightTurnFinishMessage":
            logger.info("Bot turn ended")
            return True
    
        elif mtype == "GameActionFightCastRequestMessage":
            logger.info("Spell casted")
            return True

        elif mtype == "SequenceStartMessage":
            if msg["authorId"] == self.id and msg["sequenceType"] == 1:
                pass
            return True
                
        elif mtype == "SequenceEndMessage":
            if msg["authorId"] == self.id and msg["sequenceType"] == 1:
                pass
            return True
            
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
            return True

        elif mtype == "GameFightSynchronizeMessage":
            self.monsters = []
            for fighter in msg["fighters"]:
                if fighter["__type__"] == "GameFightCharacterInformations" and int(fighter["contextualId"]) == self.bot.characterId:
                    self.currCellId = fighter["disposition"]["cellId"]
                    for characteristic in fighter["stats"]["characteristics"]["characteristics"]:
                        value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                            characteristic["objectsAndMountBonus"]
                        if characteristic["characteristicId"] == 23:
                            self.bot.currPM = value - characteristic["used"]
                        elif characteristic["characteristicId"] == 1:
                            self.bot.currPA = value - characteristic["used"]
                elif fighter["__type__"] == "GameFightMonsterInformations":
                    self.monsters.append({
                            "cellID": fighter["disposition"]["cellId"],
                            "summoned": fighter["stats"]["summoned"]
                    })  
            return True