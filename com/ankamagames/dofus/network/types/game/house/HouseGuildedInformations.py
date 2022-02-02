from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class HouseGuildedInformations(HouseInstanceInformations):
    guildInfo:GuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    