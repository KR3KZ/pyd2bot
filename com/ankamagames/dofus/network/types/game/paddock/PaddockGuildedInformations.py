from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class PaddockGuildedInformations(PaddockBuyableInformations):
    protocolId = 6908
    deserted:bool
    guildInfo:GuildInformations
    
    
