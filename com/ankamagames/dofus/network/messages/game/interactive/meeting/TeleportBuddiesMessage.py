from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportBuddiesMessage(NetworkMessage):
    dungeonId:int
    

    def init(self, dungeonId:int):
        self.dungeonId = dungeonId
        
        super().__init__()
    
    