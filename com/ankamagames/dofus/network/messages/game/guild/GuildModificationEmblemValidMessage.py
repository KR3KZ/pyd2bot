from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildModificationEmblemValidMessage(NetworkMessage):
    protocolId = 3249
    guildEmblem:GuildEmblem
    
