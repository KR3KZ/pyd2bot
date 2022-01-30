from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectsDeletedMessage(INetworkMessage):
    protocolId = 9871
    objectUID:int
    
    
