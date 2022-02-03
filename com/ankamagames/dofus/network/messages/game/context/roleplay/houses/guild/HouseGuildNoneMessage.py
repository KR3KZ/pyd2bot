from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildNoneMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    

    def init(self, houseId:int, instanceId:int, secondHand:bool):
        self.houseId = houseId
        self.instanceId = instanceId
        self.secondHand = secondHand
        
        super().__init__()
    
    