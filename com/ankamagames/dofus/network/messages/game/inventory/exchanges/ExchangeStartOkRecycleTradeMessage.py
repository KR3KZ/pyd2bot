from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkRecycleTradeMessage(NetworkMessage):
    percentToPrism:int
    percentToPlayer:int
    

    def init(self, percentToPrism:int, percentToPlayer:int):
        self.percentToPrism = percentToPrism
        self.percentToPlayer = percentToPlayer
        
        super().__init__()
    
    