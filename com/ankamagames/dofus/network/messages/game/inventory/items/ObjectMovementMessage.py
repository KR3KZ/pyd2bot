from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectMovementMessage(INetworkMessage):
    protocolId = 3421
    objectUID:int
    position:int
    
    
