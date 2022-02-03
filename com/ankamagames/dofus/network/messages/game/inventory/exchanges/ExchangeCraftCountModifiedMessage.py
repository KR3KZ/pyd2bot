from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftCountModifiedMessage(NetworkMessage):
    count:int
    

    def init(self, count:int):
        self.count = count
        
        super().__init__()
    
    