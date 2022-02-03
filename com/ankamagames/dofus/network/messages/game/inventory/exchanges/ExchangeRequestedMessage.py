from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeRequestedMessage(NetworkMessage):
    exchangeType:int
    

    def init(self, exchangeType:int):
        self.exchangeType = exchangeType
        
        super().__init__()
    
    