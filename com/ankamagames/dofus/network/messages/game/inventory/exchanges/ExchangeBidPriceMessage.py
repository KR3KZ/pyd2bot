from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidPriceMessage(NetworkMessage):
    genericId:int
    averagePrice:int
    

    def init(self, genericId:int, averagePrice:int):
        self.genericId = genericId
        self.averagePrice = averagePrice
        
        super().__init__()
    
    