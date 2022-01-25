import logging
from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.logic.frames import IFrame
logger = logging.getLogger("bot")


class RolePlayMovementFrame(IFrame):

    def process(self, mtype, msg) -> bool:
        
        if mtype == "MapComplementaryInformationsDataMessage":
            logger.debug("Map Complementary Informations Data Message received")
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
                        
            return True
                
        elif mtype == "CurrentMapMessage":
            self.bot.currMapId = int(msg["mapId"])
            logger.info('CurrentMapMessage received for mapId: {}'.format(self.bot.currMapId))
            self.bot.currMap = MapLoader.load(self.bot.currMapId)
            if self.bot.currMap:
                logger.info('Map with id {0} loaded successfully'.format(self.bot.currMapId))
            else:
                logger.error('Map with id {0} not found'.format(self.bot.currMapId))
                self.conn.interrupt()
            self.conn.send({
                '__type__': 'MapInformationsRequestMessage', 
                'mapId': self.bot.currMapId
            })
            logger.debug('MapInformationsRequestMessage sent')
            return True
            
        elif mtype == "GameMapMovementRequestMessage":
            return True
                    
        elif mtype == "ChatClientMultiMessage":
            return True
        
        return False