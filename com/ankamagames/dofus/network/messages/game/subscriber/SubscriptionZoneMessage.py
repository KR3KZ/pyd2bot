from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SubscriptionZoneMessage(NetworkMessage):
    active:bool
    

    def init(self, active:bool):
        self.active = active
        
        super().__init__()
    
    