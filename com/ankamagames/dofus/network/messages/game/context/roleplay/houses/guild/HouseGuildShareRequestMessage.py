from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    

    def init(self, houseId:int, instanceId:int, enable:bool, rights:int):
        self.houseId = houseId
        self.instanceId = instanceId
        self.enable = enable
        self.rights = rights
        
        super().__init__()
    
    