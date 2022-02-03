from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMoneyMovementInformationMessage(NetworkMessage):
    limit:int
    

    def init(self, limit:int):
        self.limit = limit
        
        super().__init__()
    
    