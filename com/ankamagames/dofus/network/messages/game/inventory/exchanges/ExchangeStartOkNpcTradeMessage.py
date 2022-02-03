from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcTradeMessage(NetworkMessage):
    npcId:int
    

    def init(self, npcId:int):
        self.npcId = npcId
        
        super().__init__()
    
    