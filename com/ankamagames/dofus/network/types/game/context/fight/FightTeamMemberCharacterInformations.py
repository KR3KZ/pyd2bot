from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberCharacterInformations(FightTeamMemberInformations):
    name:str
    level:int
    

    def init(self, name:str, level:int, id:int):
        self.name = name
        self.level = level
        
        super().__init__(id)
    
    