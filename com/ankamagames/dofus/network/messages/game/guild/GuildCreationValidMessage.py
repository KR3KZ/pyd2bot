from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class GuildCreationValidMessage(INetworkMessage):
    protocolId = 1395
    guildName:str
    guildEmblem:GuildEmblem
    
    
