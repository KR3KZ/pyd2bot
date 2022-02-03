from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
    name:str
    

    def init(self, name:str, id:int, wave:int, level:int, breed:int):
        self.name = name
        
        super().__init__(id, wave, level, breed)
    
    