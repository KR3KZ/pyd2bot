from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberEntityInformation(FightTeamMemberInformations):
    entityModelId:int
    level:int
    masterId:int
    

    def init(self, entityModelId:int, level:int, masterId:int, id:int):
        self.entityModelId = entityModelId
        self.level = level
        self.masterId = masterId
        
        super().__init__(id)
    
    