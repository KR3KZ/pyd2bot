from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberMonsterInformations(FightTeamMemberInformations):
    monsterId:int
    grade:int
    

    def init(self, monsterId:int, grade:int, id:int):
        self.monsterId = monsterId
        self.grade = grade
        
        super().__init__(id)
    
    