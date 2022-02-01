from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatErrorMessage(INetworkMessage):
    protocolId = 5479
    reason:int
    
    
