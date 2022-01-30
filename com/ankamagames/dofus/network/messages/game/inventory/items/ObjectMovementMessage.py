from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectMovementMessage(NetworkMessage):
    protocolId = 3421
    objectUID:int
    position:int
    
