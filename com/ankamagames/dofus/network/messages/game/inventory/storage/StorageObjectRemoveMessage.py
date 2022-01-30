from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StorageObjectRemoveMessage(NetworkMessage):
    protocolId = 4970
    objectUID:int
    
