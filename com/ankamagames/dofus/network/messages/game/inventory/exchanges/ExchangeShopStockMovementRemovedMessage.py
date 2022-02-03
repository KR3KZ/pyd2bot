from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeShopStockMovementRemovedMessage(NetworkMessage):
    objectId:int
    

    def init(self, objectId:int):
        self.objectId = objectId
        
        super().__init__()
    
    