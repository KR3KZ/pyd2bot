from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeHandleMountsMessage(NetworkMessage):
    actionType:int
    ridesId:list[int]
    

    def init(self, actionType:int, ridesId:list[int]):
        self.actionType = actionType
        self.ridesId = ridesId
        
        super().__init__()
    
    