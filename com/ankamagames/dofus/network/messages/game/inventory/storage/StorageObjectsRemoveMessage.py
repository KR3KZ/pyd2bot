from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StorageObjectsRemoveMessage(NetworkMessage):
    protocolId = 7044
    objectUIDList:int
    
