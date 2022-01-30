from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectMovementMessage(INetworkMessage):
    protocolId = 3421
    objectUID:int
    position:int
    
    
