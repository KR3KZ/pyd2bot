from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectDeleteMessage(NetworkMessage):
    protocolId = 8147
    objectUID:int
    quantity:int
    
    
