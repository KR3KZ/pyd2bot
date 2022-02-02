from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


@dataclass
class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
    firstNameId:int
    lastNameId:int
    level:int
    guildId:int
    uid:int
    
    
    def __post_init__(self):
        super().__init__()
    