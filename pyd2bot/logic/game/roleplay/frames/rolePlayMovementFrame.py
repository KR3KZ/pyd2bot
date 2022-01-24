import logging
import pyd2bot.bot as bot
from pyd2bot.gameData.mapReader import MapLoader
logger = logging.getLogger("bot")


class RolePlayMovementFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "MapComplementaryInformationsDataMessage":
            bot.Bot.currMapInteractiveElems  = {}
            bot.Bot.currMapStatedElems = {}
            
            for ielem in msg["interactiveElements"]:
                bot.Bot.currMapInteractiveElems[ielem["elementId"]] = ielem
            
            for selem in msg["statedElements"]:
                bot.Bot.currMapStatedElems[selem["elementId"]] = selem
            
            for actor in msg["actors"]:
                if actor["__type__"] == "GameRolePlayCharacterInformations":
                    if actor["name"] == bot.Bot.characterName and actor["contextualId"] == bot.Bot.characterID:
                        bot.Bot.currCellId = actor["disposition"]["cellId"]
                        bot.Bot.direction = actor["disposition"]["direction"]
                        
            bot.Bot.mapDataReceived.set()
            return True
                
        elif mtype == "CurrentMapMessage":
            print('CurrentMapMessage received')
            bot.Bot.currMapId = int(msg["mapId"])
            bot.Bot.currMap = MapLoader.load(bot.Bot.currMapId)
            bot.Bot.onMap.set()
            return True
            
        elif mtype == "GameMapMovementRequestMessage":
            bot.Bot.moving.set()
            bot.Bot.idle.clear()
            return True
            
        elif mtype == "GameMapMovementConfirmMessage":
            bot.Bot.moving.clear()
            bot.Bot.idle.set()
            return True
                    
        elif mtype == "ChatClientMultiMessage":
            return True