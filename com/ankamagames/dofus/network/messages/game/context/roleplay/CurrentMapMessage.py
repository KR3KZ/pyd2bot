from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CurrentMapMessage(NetworkMessage):
    mapId:int
    mapKey:str
    

    def init(self, mapId:int, mapKey:str):
        self.mapId = mapId
        self.mapKey = mapKey
        
        super().__init__()
    
    