from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicStatMessage(NetworkMessage):
    timeSpent:int
    statId:int
    

    def init(self, timeSpent:int, statId:int):
        self.timeSpent = timeSpent
        self.statId = statId
        
        super().__init__()
    
    