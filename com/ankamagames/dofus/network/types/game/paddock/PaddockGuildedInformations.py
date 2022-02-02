from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class PaddockGuildedInformations(PaddockBuyableInformations):
    deserted:bool
    guildInfo:GuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    