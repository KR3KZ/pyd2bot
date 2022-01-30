from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    protocolId = 5107
    objectUID:int
    position:int
    quantity:int
    
    
