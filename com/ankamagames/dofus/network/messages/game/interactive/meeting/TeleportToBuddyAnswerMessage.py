from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyAnswerMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    accept:bool
    

    def init(self, dungeonId:int, buddyId:int, accept:bool):
        self.dungeonId = dungeonId
        self.buddyId = buddyId
        self.accept = accept
        
        super().__init__()
    
    