from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlag(NetworkMessage):
    mapId:int
    state:int
    

    def init(self, mapId:int, state:int):
        self.mapId = mapId
        self.state = state
        
        super().__init__()
    
    