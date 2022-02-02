from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


@dataclass
class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
    allianceInfos:BasicAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    