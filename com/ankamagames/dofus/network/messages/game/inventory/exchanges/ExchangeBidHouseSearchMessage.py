from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseSearchMessage(NetworkMessage):
    genId:int
    follow:bool
    

    def init(self, genId_:int, follow_:bool):
        self.genId = genId_
        self.follow = follow_
        
        super().__init__()
    
    