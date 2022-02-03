from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageObjectsRemoveMessage(NetworkMessage):
    objectUIDList:list[int]
    

    def init(self, objectUIDList:list[int]):
        self.objectUIDList = objectUIDList
        
        super().__init__()
    
    