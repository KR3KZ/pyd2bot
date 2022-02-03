from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseGuildedInformations(HouseInstanceInformations):
    guildInfo:'GuildInformations'
    

    def init(self, guildInfo:'GuildInformations', instanceId:int, ownerTag:'AccountTagInformation', price:int):
        self.guildInfo = guildInfo
        
        super().__init__(instanceId, ownerTag, price)
    
    