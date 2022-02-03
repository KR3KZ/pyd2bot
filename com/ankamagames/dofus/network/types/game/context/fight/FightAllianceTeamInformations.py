from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
    


class FightAllianceTeamInformations(FightTeamInformations):
    relation:int
    

    def init(self, relation:int, teamMembers:list['FightTeamMemberInformations'], teamId:int, leaderId:int, teamSide:int, teamTypeId:int, nbWaves:int):
        self.relation = relation
        
        super().__init__(teamMembers, teamId, leaderId, teamSide, teamTypeId, nbWaves)
    
    