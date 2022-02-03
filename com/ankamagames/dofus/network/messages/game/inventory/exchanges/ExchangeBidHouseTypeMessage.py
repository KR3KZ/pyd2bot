from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseTypeMessage(NetworkMessage):
    type:int
    follow:bool
    

    def init(self, type_:int, follow_:bool):
        self.type = type_
        self.follow = follow_
        
        super().__init__()
    
    