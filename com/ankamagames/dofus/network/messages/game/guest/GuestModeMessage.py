from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuestModeMessage(NetworkMessage):
    active:bool
    

    def init(self, active:bool):
        self.active = active
        
        super().__init__()
    
    