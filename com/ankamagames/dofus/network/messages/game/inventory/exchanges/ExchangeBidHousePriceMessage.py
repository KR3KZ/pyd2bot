from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHousePriceMessage(NetworkMessage):
    genId:int
    

    def init(self, genId:int):
        self.genId = genId
        
        super().__init__()
    
    