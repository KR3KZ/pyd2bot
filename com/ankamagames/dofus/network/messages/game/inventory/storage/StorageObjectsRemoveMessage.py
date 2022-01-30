from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StorageObjectsRemoveMessage(INetworkMessage):
    protocolId = 7044
    objectUIDList:int
    
    
