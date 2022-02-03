from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountDataErrorMessage(NetworkMessage):
    reason:int
    

    def init(self, reason:int):
        self.reason = reason
        
        super().__init__()
    
    