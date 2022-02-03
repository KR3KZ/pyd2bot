from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeErrorMessage(NetworkMessage):
    errorType:int
    

    def init(self, errorType:int):
        self.errorType = errorType
        
        super().__init__()
    
    