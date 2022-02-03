from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportHavenBagRequestMessage(NetworkMessage):
    guestId:int
    

    def init(self, guestId:int):
        self.guestId = guestId
        
        super().__init__()
    
    