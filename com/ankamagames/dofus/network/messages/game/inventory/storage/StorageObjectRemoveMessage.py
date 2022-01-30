from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StorageObjectRemoveMessage(INetworkMessage):
    protocolId = 4970
    objectUID:int
    
    
