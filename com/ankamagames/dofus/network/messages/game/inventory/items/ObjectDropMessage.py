from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectDropMessage(INetworkMessage):
    protocolId = 5971
    objectUID:int
    quantity:int
    
    
