from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class HumanOptionGuild(HumanOption):
    guildInformations:GuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    