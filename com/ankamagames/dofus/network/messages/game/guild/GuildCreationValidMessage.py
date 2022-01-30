from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildCreationValidMessage(NetworkMessage):
    protocolId = 1395
    guildName:str
    guildEmblem:GuildEmblem
    
