from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModifiedMessage(NetworkMessage):
    goldSum:int
    

    def init(self, goldSum:int):
        self.goldSum = goldSum
        
        super().__init__()
    
    