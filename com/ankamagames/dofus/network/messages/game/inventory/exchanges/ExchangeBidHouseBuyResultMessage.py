from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    uid:int
    bought:bool
    

    def init(self, uid:int, bought:bool):
        self.uid = uid
        self.bought = bought
        
        super().__init__()
    
    