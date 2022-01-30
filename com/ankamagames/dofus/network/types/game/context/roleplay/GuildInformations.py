from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildInformations(BasicGuildInformations):
    protocolId = 1201
    guildEmblem:GuildEmblem
    
