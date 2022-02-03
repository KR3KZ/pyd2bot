from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ZaapRespawnUpdatedMessage(NetworkMessage):
    mapId:int
    

    def init(self, mapId:int):
        self.mapId = mapId
        
        super().__init__()
    
    