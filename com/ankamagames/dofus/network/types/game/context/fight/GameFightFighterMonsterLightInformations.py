from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
    creatureGenericId:int
    

    def init(self, creatureGenericId:int, id:int, wave:int, level:int, breed:int):
        self.creatureGenericId = creatureGenericId
        
        super().__init__(id, wave, level, breed)
    
    