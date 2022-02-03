from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageObjectRemoveMessage(NetworkMessage):
    objectUID:int
    

    def init(self, objectUID:int):
        self.objectUID = objectUID
        
        super().__init__()
    
    