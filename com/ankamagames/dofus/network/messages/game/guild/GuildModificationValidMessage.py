from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildModificationValidMessage(INetworkMessage):
    protocolId = 7329
    guildName:str
    guildEmblem:GuildEmblem
    
    
