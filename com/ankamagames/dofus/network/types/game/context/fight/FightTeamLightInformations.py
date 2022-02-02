from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations


@dataclass
class FightTeamLightInformations(AbstractFightTeamInformations):
    teamMembersCount:int
    meanLevel:int
    hasFriend:bool
    hasGuildMember:bool
    hasAllianceMember:bool
    hasGroupMember:bool
    hasMyTaxCollector:bool
    
    
    def __post_init__(self):
        super().__init__()
    