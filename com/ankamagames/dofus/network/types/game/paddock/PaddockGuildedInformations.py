from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class PaddockGuildedInformations(PaddockBuyableInformations):
    deserted:bool
    guildInfo:'GuildInformations'
    

    def init(self, deserted:bool, guildInfo:'GuildInformations', price:int, locked:bool):
        self.deserted = deserted
        self.guildInfo = guildInfo
        
        super().__init__(price, locked)
    
    