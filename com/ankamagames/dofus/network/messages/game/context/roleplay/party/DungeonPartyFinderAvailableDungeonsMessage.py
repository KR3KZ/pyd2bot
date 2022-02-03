from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(NetworkMessage):
    dungeonIds:list[int]
    

    def init(self, dungeonIds:list[int]):
        self.dungeonIds = dungeonIds
        
        super().__init__()
    
    