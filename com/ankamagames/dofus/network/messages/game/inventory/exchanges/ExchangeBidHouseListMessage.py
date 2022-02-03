from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseListMessage(NetworkMessage):
    id:int
    follow:bool
    

    def init(self, id:int, follow:bool):
        self.id = id
        self.follow = follow
        
        super().__init__()
    
    