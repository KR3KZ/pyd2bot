from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


@dataclass
class AlliancedGuildFactSheetInformations(GuildInformations):
    allianceInfos:BasicNamedAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    