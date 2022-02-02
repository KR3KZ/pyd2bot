from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.GuildFactsMessage import GuildFactsMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


@dataclass
class GuildInAllianceFactsMessage(GuildFactsMessage):
    allianceInfos:BasicNamedAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    