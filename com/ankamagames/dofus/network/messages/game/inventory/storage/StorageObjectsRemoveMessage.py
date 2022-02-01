from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageObjectsRemoveMessage(NetworkMessage):
    objectUIDList:list[int]
    
    
