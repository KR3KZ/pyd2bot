from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeMapMessage(NetworkMessage):
    mapId:int
    autopilot:bool
    

    def init(self, mapId:int, autopilot:bool):
        self.mapId = mapId
        self.autopilot = autopilot
        
        super().__init__()
    
    