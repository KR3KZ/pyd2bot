from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectSetPositionMessage(INetworkMessage):
    protocolId = 5107
    objectUID:int
    position:int
    quantity:int
    
    
