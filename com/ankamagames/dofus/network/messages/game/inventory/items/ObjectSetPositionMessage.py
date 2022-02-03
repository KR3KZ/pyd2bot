from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    objectUID:int
    position:int
    quantity:int
    

    def init(self, objectUID:int, position:int, quantity:int):
        self.objectUID = objectUID
        self.position = position
        self.quantity = quantity
        
        super().__init__()
    
    