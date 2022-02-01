from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IgnoredDeleteRequestMessage(INetworkMessage):
    protocolId = 2264
    accountId:int
    session:bool
    
    
