from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


@dataclass
class FightTeamInformations(AbstractFightTeamInformations):
    teamMembers:list[FightTeamMemberInformations]
    
    
    def __post_init__(self):
        super().__init__()
    