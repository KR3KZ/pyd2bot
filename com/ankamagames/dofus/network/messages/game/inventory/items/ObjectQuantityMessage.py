from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectQuantityMessage(NetworkMessage):
    objectUID:int
    quantity:int
    origin:int
    

    def init(self, objectUID:int, quantity:int, origin:int):
        self.objectUID = objectUID
        self.quantity = quantity
        self.origin = origin
        
        super().__init__()
    
    