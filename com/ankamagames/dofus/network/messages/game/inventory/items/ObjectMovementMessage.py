from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectMovementMessage(NetworkMessage):
    objectUID:int
    position:int
    

    def init(self, objectUID:int, position:int):
        self.objectUID = objectUID
        self.position = position
        
        super().__init__()
    
    