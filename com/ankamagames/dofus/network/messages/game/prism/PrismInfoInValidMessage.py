from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInfoInValidMessage(NetworkMessage):
    reason:int
    

    def init(self, reason:int):
        self.reason = reason
        
        super().__init__()
    
    