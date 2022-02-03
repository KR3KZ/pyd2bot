from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBuyMessage(NetworkMessage):
    objectToBuyId:int
    quantity:int
    

    def init(self, objectToBuyId:int, quantity:int):
        self.objectToBuyId = objectToBuyId
        self.quantity = quantity
        
        super().__init__()
    
    