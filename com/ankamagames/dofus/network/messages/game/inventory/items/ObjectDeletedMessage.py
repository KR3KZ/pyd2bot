from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectDeletedMessage(INetworkMessage):
    protocolId = 7574
    objectUID:int
    
    
