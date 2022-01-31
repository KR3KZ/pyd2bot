from pyd2bot.logic.frames import IFrame
from com.ankamagames.jerakine.logger.Logger import Logger
logger = Logger(__name__)


class RolePlayInteractiveFrame(IFrame):


    def process(self, mtype, msg) -> bool:
        
        if mtype == "InteractiveUseErrorMessage":
            self.bot.farmingError.set()
            self.bot.farming.set()
            self.bot.idle.set()
            return True
        
        elif mtype == "InteractiveUsedMessage":
            skill = msg["skillId"]
            self.bot.currFarmingElem = msg["elemId"]
            self.bot.farming.set()
            self.bot.idle.clear()
            logger.info(f"Farming animation of elem {self.bot.currFarmingElem} with skill {skill} started")
            return True
        
        elif mtype == "InteractiveUseEndedMessage":
            logger.info(f"Farming animation of elem {self.bot.currFarmingElem} ended")            
            self.bot.currFarmingElem = None
            self.bot.farming.clear()
            self.bot.idle.set()
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