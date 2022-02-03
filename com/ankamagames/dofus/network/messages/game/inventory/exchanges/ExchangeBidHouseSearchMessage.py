from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseSearchMessage(NetworkMessage):
    genId:int
    follow:bool
    

    def init(self, genId:int, follow:bool):
        self.genId = genId
        self.follow = follow
        
        super().__init__()
    
    