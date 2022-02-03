from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectsDeletedMessage(NetworkMessage):
    objectUID:list[int]
    

    def init(self, objectUID:list[int]):
        self.objectUID = objectUID
        
        super().__init__()
    
    