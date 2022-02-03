from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(NetworkMessage):
    sellerId:int
    

    def init(self, sellerId:int):
        self.sellerId = sellerId
        
        super().__init__()
    
    