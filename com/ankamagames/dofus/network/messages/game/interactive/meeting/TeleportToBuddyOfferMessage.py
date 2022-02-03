from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    timeLeft:int
    

    def init(self, dungeonId:int, buddyId:int, timeLeft:int):
        self.dungeonId = dungeonId
        self.buddyId = buddyId
        self.timeLeft = timeLeft
        
        super().__init__()
    
    