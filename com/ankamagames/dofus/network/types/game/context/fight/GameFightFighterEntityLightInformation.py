from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterEntityLightInformation(GameFightFighterLightInformations):
    entityModelId:int
    masterId:int
    

    def init(self, entityModelId:int, masterId:int, id:int, wave:int, level:int, breed:int):
        self.entityModelId = entityModelId
        self.masterId = masterId
        
        super().__init__(id, wave, level, breed)
    
    