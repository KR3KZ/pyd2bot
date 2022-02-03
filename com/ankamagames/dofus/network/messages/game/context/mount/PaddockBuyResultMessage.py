from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyResultMessage(NetworkMessage):
    paddockId:int
    bought:bool
    realPrice:int
    

    def init(self, paddockId:int, bought:bool, realPrice:int):
        self.paddockId = paddockId
        self.bought = bought
        self.realPrice = realPrice
        
        super().__init__()
    
    