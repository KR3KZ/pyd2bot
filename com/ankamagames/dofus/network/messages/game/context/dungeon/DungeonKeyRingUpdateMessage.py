from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingUpdateMessage(NetworkMessage):
    dungeonId:int
    available:bool
    

    def init(self, dungeonId:int, available:bool):
        self.dungeonId = dungeonId
        self.available = available
        
        super().__init__()
    
    