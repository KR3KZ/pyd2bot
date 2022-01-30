from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectDeletedMessage(NetworkMessage):
    protocolId = 7574
    objectUID:int
    
