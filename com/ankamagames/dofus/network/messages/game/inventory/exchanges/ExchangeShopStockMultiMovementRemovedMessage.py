from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(NetworkMessage):
    objectIdList:list[int]
    

    def init(self, objectIdList:list[int]):
        self.objectIdList = objectIdList
        
        super().__init__()
    
    