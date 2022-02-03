from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightSwapRequestMessage(NetworkMessage):
    subAreaId:int
    targetId:int
    

    def init(self, subAreaId:int, targetId:int):
        self.subAreaId = subAreaId
        self.targetId = targetId
        
        super().__init__()
    
    