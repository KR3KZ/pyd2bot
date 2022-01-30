from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamInformations(AbstractFightTeamInformations):
    protocolId = 4654
    teamMembers:FightTeamMemberInformations
    
    
