from pyd2bot.logic.frames import IFrame
import logging
logger = logging.getLogger("bot")


class RolePlayInteractiveFrame(IFrame):


    def process(self, mtype, msg) -> bool:
        
        if mtype == "InteractiveUseErrorMessage":
            self.bot.farmingError.set()
            return True
        
        elif mtype == "InteractiveUsedMessage":
            skill = msg["skillId"]
            self.bot.currFarmingElem = msg["elemId"]
            logger.info(f"Farming animation of elem {self.bot.currFarmingElem} with skill {skill} started")
            return True
        
        elif mtype == "InteractiveUseEndedMessage":
            logger.info(f"Farming animation of elem {self.bot.currFarmingElem} ended")            
            self.bot.currFarmingElem = None
            return True
    
        elif mtype == "StatedElementUpdatedMessage":
            elem_id = msg["statedElement"]["elementId"]
            self.bot.currMapStatedElems[elem_id] = msg["statedElement"]
            logger.debug(f"Element {elem_id} state changed")
            return True
        
        elif mtype == "InteractiveElementUpdatedMessage":
            elem_id = msg["interactiveElement"]["elementId"]
            self.bot.currMapInteractiveElems[elem_id] = msg["interactiveElement"]
            logger.debug(f"Element {elem_id} interactiveness changed")
            return True
        
        return False