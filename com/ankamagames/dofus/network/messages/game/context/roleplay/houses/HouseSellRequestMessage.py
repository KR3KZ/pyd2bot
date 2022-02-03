from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    instanceId:int
    amount:int
    forSale:bool
    

    def init(self, instanceId:int, amount:int, forSale:bool):
        self.instanceId = instanceId
        self.amount = amount
        self.forSale = forSale
        
        super().__init__()
    
    