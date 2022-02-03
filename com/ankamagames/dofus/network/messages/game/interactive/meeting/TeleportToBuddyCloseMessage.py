from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyCloseMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    

    def init(self, dungeonId:int, buddyId:int):
        self.dungeonId = dungeonId
        self.buddyId = buddyId
        
        super().__init__()
    
    