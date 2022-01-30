from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class HouseGuildedInformations(HouseInstanceInformations):
    protocolId = 856
    guildInfo:GuildInformations
    
