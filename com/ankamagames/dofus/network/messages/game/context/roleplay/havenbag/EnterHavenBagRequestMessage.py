from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EnterHavenBagRequestMessage(NetworkMessage):
    havenBagOwner:int
    

    def init(self, havenBagOwner:int):
        self.havenBagOwner = havenBagOwner
        
        super().__init__()
    
    