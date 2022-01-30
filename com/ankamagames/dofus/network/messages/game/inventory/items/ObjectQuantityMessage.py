from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectQuantityMessage(NetworkMessage):
    protocolId = 80
    objectUID:int
    quantity:int
    origin:int
    
