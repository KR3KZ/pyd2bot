from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
    


class FightTeamInformations(AbstractFightTeamInformations):
    teamMembers:list['FightTeamMemberInformations']
    

    def init(self, teamMembers:list['FightTeamMemberInformations'], teamId:int, leaderId:int, teamSide:int, teamTypeId:int, nbWaves:int):
        self.teamMembers = teamMembers
        
        super().__init__(teamId, leaderId, teamSide, teamTypeId, nbWaves)
    
    