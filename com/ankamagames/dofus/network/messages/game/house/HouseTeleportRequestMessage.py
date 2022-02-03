from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseTeleportRequestMessage(NetworkMessage):
    houseId:int
    houseInstanceId:int
    

    def init(self, houseId:int, houseInstanceId:int):
        self.houseId = houseId
        self.houseInstanceId = houseInstanceId
        
        super().__init__()
    
    