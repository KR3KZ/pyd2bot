from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectQuantityMessage(INetworkMessage):
    protocolId = 80
    objectUID:int
    quantity:int
    origin:int
    
    
