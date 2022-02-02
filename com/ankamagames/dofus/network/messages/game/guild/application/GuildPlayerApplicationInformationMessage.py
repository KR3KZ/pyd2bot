from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


@dataclass
class GuildPlayerApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
    guildInformation:GuildInformations
    apply:GuildApplicationInformation
    
    
    def __post_init__(self):
        super().__init__()
    