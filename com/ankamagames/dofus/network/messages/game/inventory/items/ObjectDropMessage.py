from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectDropMessage(NetworkMessage):
    protocolId = 5971
    objectUID:int
    quantity:int
    
