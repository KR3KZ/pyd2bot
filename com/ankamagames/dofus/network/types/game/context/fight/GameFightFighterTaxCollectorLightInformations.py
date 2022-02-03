from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterTaxCollectorLightInformations(GameFightFighterLightInformations):
    firstNameId:int
    lastNameId:int
    

    def init(self, firstNameId:int, lastNameId:int, id:int, wave:int, level:int, breed:int):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        
        super().__init__(id, wave, level, breed)
    
    