from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildRightsViewMessage(NetworkMessage):
    houseId:int
    instanceId:int
    

    def init(self, houseId:int, instanceId:int):
        self.houseId = houseId
        self.instanceId = instanceId
        
        super().__init__()
    
    