import logging
from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.logic import IFrame
logger = logging.getLogger("bot")


class RolePlayMovementFrame(IFrame):


    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "MapComplementaryInformationsDataMessage":
            self.bot.currMapInteractiveElems  = {}
            self.bot.currMapStatedElems = {}
            
            for ielem in msg["interactiveElements"]:
                self.bot.currMapInteractiveElems[ielem["elementId"]] = ielem
            
            for selem in msg["statedElements"]:
                self.bot.currMapStatedElems[selem["elementId"]] = selem
            
            for actor in msg["actors"]:
                if actor["__type__"] == "GameRolePlayCharacterInformations":
                    if actor["name"] == self.bot.name and actor["contextualId"] == self.bot.characterID:
                        self.bot.currCellId = actor["disposition"]["cellId"]
                        self.bot.direction = actor["disposition"]["direction"]
                        
            self.bot.mapDataReceived.set()
            return True
                
        elif mtype == "CurrentMapMessage":
            logger.info('CurrentMapMessage received')
            self.bot.currMapId = int(msg["mapId"])
            self.bot.currMap = MapLoader.load(self.bot.currMapId)
            self.bot.onMap.set()
            self.bot.mapDataReceived.clear()
            self.conn.send({
                '__type__': 'MapInformationsRequestMessage', 
                'mapId': self.bot.currMapId
            })
            return True
            
        elif mtype == "GameMapMovementRequestMessage":
            self.bot.moving.set()
            self.bot.idle.clear()
            return True
                    
        elif mtype == "ChatClientMultiMessage":
            return True
        
        return False