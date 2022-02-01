from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildUpdateApplicationMessage(INetworkMessage):
    protocolId = 6940
    applyText:str
    guildId:int
    
    
