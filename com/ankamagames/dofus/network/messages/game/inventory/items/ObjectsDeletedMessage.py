from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectsDeletedMessage(NetworkMessage):
    protocolId = 9871
    objectUID:int
    
    
