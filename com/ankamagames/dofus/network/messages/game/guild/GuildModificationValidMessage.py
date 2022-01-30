from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildModificationValidMessage(NetworkMessage):
    protocolId = 7329
    guildName:str
    guildEmblem:GuildEmblem
    
    
