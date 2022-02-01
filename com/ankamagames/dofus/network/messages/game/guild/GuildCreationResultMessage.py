from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildCreationResultMessage(INetworkMessage):
    protocolId = 42
    result:int
    
    
