from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectErrorMessage(INetworkMessage):
    protocolId = 9603
    reason:int
    
    
