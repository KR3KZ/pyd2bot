from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ErrorMapNotFoundMessage(NetworkMessage):
    mapId:int
    

    def init(self, mapId:int):
        self.mapId = mapId
        
        super().__init__()
    
    