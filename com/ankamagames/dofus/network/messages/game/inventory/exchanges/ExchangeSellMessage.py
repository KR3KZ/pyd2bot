from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeSellMessage(NetworkMessage):
    objectToSellId:int
    quantity:int
    

    def init(self, objectToSellId:int, quantity:int):
        self.objectToSellId = objectToSellId
        self.quantity = quantity
        
        super().__init__()
    
    