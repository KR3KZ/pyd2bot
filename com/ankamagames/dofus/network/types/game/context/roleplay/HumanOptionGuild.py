from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class HumanOptionGuild(HumanOption):
    protocolId = 1437
    guildInformations:GuildInformations
    
    
