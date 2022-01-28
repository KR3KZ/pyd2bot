from damageCalculation.tools import StatIds
from pyd2bot.gameData.enums.playerTypeEnum import PlayerTypeEnum

import logging
logger = logging.getLogger("bot")

class GameFightFrame(IFrame):
    

    def process(self, mtype, msg) -> bool:
        
        if not self.bot.isInFight.is_set():
            return False 

        elif mtype == "GameFightShowFighterMessage":
            return True
        
        elif mtype == "GameFightTurnReadyRequestMessage":
            if int(msg["id"]) == self.bot.characterId:
                self.bot.isTurn.set()

        elif mtype == "GameFightTurnEndMessage":
            if int(msg["id"]) == self.bot.characterId:
                self.bot.turnEnded.set()
                self.bot.turnStarted.clear()
                self.bot.isTurn.clear()

        elif mtype == "GameFightEndMessage":
            self.bot.isInFight.clear()
            return True

        elif mtype == "GameFightTurnStartPlayingMessage":
            logger.info("Bot turn started")
            self.bot.turnStarted.set()
            return True
        
        elif mtype == "GameFightTurnFinishMessage":
            logger.info("Bot turn ended")
            return True
    
        elif mtype == "GameActionFightCastRequestMessage":
            logger.info("Spell casted")
            return True

        elif mtype == "SequenceStartMessage":
            if int(msg["authorId"]) == self.bot.characterId and msg["sequenceType"] == 1:
                pass
            return True
                
        elif mtype == "SequenceEndMessage":
            if int(msg["authorId"]) == self.bot.characterId and msg["sequenceType"] == 1:
                pass
            return True
            
        elif mtype == "RefreshCharacterStatsMessage":
            if msg["fighterId"] == self.bot.characterId:
                for characteristic in msg["stats"]["characteristics"]["characteristics"]:
                    value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                            characteristic["objectsAndMountBonus"]
                    if characteristic["characteristicId"] == 23:
                        self.bot.currPM = int(value - characteristic["used"])
                    elif characteristic["characteristicId"] == 1:
                        self.bot.currPA = int(value - characteristic["used"])
                logger.info(f"Bot pa, pm: {self.bot.currPA, self.bot.currPM}")
            return True

        elif mtype == "GameFightSynchronizeMessage":
            currMap = self.bot.currMap
            currMap.entities = {}
            for fighter in msg["fighters"]:
                fcellId = fighter["disposition"]["cellId"]
                currMap.entities[fcellId] = {
                    "id": int(fighter["contextualId"]),
                    "invisibilityState": fighter["stats"]["invisibilityState"],
                    "summoned": fighter["stats"]["summoned"]
                }
                if fighter["__type__"] == "GameFightCharacterInformations" and int(fighter["contextualId"]) == self.bot.characterId:
                    self.currCellId = fcellId
                    currMap.entities[fcellId]["level"] = fighter["stats"]["level"]
                    currMap.entities[fcellId]["type"] = PlayerTypeEnum.HUMAN
                    for characteristic in fighter["stats"]["characteristics"]["characteristics"]:
                        value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                            characteristic["objectsAndMountBonus"]
                        if characteristic["characteristicId"] == StatIds.ACTION_POINTS:
                            self.bot.currPM = int(value - characteristic["used"])
                        elif characteristic["characteristicId"] == StatIds.MOVEMENT_POINTS:
                            self.bot.currPA = int(value - characteristic["used"])
                else:
                    currMap.entities[fcellId]["type"] = PlayerTypeEnum.MONSTER
                    currMap.entities[fcellId]["level"] = fighter["stats"]["creatureLevel"]
            return True

        elif mtype == "GameEntitiesDispositionMessage":
            for disposition in msg["dispositions"]:
                cellId = disposition["cellId"]
                self.bot.currMap.entities[cellId]["id"] = int(disposition["id"])
            return True
        
        elif mtype == "GameMapMovementMessage":
            startCellId = int(msg["keyMovements"][0]) & 4095
            endCellId = int(msg["keyMovements"][-1]) & 4095
            entity = self.bot.currMap.entities.pop(startCellId)
            self.bot.currMap.entities[endCellId] = entity
            return True