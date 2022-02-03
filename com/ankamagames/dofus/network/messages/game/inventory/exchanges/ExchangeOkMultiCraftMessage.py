from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    initiatorId:int
    otherId:int
    role:int
    

    def init(self, initiatorId:int, otherId:int, role:int):
        self.initiatorId = initiatorId
        self.otherId = otherId
        self.role = role
        
        super().__init__()
    
    