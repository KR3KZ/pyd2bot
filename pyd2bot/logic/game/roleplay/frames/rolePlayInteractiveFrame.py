import logging
logger = logging.getLogger("bot")
import pyd2bot.bot as bot

class RolePlayInteractiveFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "InteractiveUseErrorMessage":
            bot.Bot.farmingError.set()
            return True
        
        elif mtype == "InteractiveUsedMessage":
            skill = msg["skillId"]
            self.currFarmingElem = msg["elemId"]
            logger.info(f"Farming animation of elem {self.currFarmingElem} with skill {skill} started")
            bot.Bot.farming.set()
            return True
        
        elif mtype == "InteractiveUseEndedMessage":
            logger.info(f"Farming animation of elem {self.currFarmingElem} ended")
            return True
    
        elif mtype == "StatedElementUpdatedMessage":
            elem_id = msg["statedElement"]["elementId"]
            bot.Bot.currMapStatedElems[elem_id] = msg["statedElement"]
            logger.info(f"Element {elem_id} state changed")
            return True
        
        elif mtype == "InteractiveElementUpdatedMessage":
            elem_id = msg["interactiveElement"]["elementId"]
            bot.Bot.currMapInteractiveElems[elem_id] = msg["interactiveElement"]
            logger.info(f"Element {elem_id} interactiveness changed")
            if self.currFarmingElem == elem_id:
                self.currFarmingElem = None
                bot.Bot.farming.clear()
            return True