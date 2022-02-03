from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobAllowMultiCraftRequestMessage(NetworkMessage):
    enabled:bool
    

    def init(self, enabled:bool):
        self.enabled = enabled
        
        super().__init__()
    
    