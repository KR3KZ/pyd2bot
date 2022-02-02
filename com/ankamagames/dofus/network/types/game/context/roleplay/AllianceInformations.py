from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


@dataclass
class AllianceInformations(BasicNamedAllianceInformations):
    allianceEmblem:GuildEmblem
    
    
    def __post_init__(self):
        super().__init__()
    