from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    sourceType:int
    destinationType:int
    mapId:int
    

    def init(self, sourceType:int, destinationType:int, mapId:int):
        self.sourceType = sourceType
        self.destinationType = destinationType
        self.mapId = mapId
        
        super().__init__()
    
    