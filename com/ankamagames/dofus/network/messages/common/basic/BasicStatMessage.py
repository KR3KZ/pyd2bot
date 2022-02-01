from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicStatMessage(INetworkMessage):
    protocolId = 514
    timeSpent:int
    statId:int
    
    
