from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


@dataclass
class GuildInformations(BasicGuildInformations):
    guildEmblem:GuildEmblem
    
    
    def __post_init__(self):
        super().__init__()
    