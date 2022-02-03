from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class KickHavenBagRequestMessage(NetworkMessage):
    guestId:int
    

    def init(self, guestId:int):
        self.guestId = guestId
        
        super().__init__()
    
    