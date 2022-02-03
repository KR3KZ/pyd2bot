from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderListenErrorMessage(NetworkMessage):
    dungeonId:int
    

    def init(self, dungeonId:int):
        self.dungeonId = dungeonId
        
        super().__init__()
    
    