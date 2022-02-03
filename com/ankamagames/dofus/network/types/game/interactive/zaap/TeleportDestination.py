from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportDestination(NetworkMessage):
    type:int
    mapId:int
    subAreaId:int
    level:int
    cost:int
    

    def init(self, type:int, mapId:int, subAreaId:int, level:int, cost:int):
        self.type = type
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.level = level
        self.cost = cost
        
        super().__init__()
    
    