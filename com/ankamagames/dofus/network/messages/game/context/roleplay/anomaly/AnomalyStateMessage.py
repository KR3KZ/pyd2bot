from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    subAreaId:int
    open:bool
    closingTime:int
    

    def init(self, subAreaId:int, open:bool, closingTime:int):
        self.subAreaId = subAreaId
        self.open = open
        self.closingTime = closingTime
        
        super().__init__()
    
    