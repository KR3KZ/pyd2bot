from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamInformations(AbstractFightTeamInformations):
    teamMembers:list[FightTeamMemberInformations]
    
    
