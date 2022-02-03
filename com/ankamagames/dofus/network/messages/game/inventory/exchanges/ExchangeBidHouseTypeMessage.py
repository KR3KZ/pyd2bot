from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseTypeMessage(NetworkMessage):
    type:int
    follow:bool
    

    def init(self, type:int, follow:bool):
        self.type = type
        self.follow = follow
        
        super().__init__()
    
    