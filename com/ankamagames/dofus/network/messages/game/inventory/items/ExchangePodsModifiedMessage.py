from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    currentWeight:int
    maxWeight:int
    

    def init(self, currentWeight:int, maxWeight:int, remote:bool):
        self.currentWeight = currentWeight
        self.maxWeight = maxWeight
        
        super().__init__(remote)
    
    