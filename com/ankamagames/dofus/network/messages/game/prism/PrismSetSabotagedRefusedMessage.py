from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSetSabotagedRefusedMessage(NetworkMessage):
    subAreaId:int
    reason:int
    

    def init(self, subAreaId:int, reason:int):
        self.subAreaId = subAreaId
        self.reason = reason
        
        super().__init__()
    
    