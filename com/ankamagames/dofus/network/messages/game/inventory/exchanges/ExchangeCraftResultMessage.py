from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftResultMessage(NetworkMessage):
    craftResult:int
    

    def init(self, craftResult:int):
        self.craftResult = craftResult
        
        super().__init__()
    
    