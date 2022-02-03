from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FriendSetStatusShareMessage(NetworkMessage):
    share:bool
    

    def init(self, share:bool):
        self.share = share
        
        super().__init__()
    
    