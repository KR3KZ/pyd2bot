from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CurrentMapMessage(NetworkMessage):
    mapId:int
    mapKey:str
    

    def init(self, mapId_:int, mapKey_:str):
        self.mapId = mapId_
        self.mapKey = mapKey_
        
        super().__init__()
    
    