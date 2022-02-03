from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    dungeonId:int
    inviterId:int
    invalidBuddiesIds:list[int]
    

    def init(self, dungeonId:int, inviterId:int, invalidBuddiesIds:list[int]):
        self.dungeonId = dungeonId
        self.inviterId = inviterId
        self.invalidBuddiesIds = invalidBuddiesIds
        
        super().__init__()
    
    