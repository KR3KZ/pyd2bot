from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseBuyResultMessage(NetworkMessage):
    houseId:int
    instanceId:int
    realPrice:int
    secondHand:bool
    bought:bool
    

    def init(self, houseId:int, instanceId:int, realPrice:int):
        self.houseId = houseId
        self.instanceId = instanceId
        self.realPrice = realPrice
        
        super().__init__()
    
    