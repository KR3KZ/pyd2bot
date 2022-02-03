from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeWeightMessage(NetworkMessage):
    currentWeight:int
    maxWeight:int
    

    def init(self, currentWeight:int, maxWeight:int):
        self.currentWeight = currentWeight
        self.maxWeight = maxWeight
        
        super().__init__()
    
    