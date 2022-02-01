from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CurrentServerStatusUpdateMessage(INetworkMessage):
    protocolId = 547
    status:int
    
    
