from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectDeletedMessage(INetworkMessage):
    protocolId = 7574
    objectUID:int
    
    
