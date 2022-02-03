from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    latency:int
    sampleCount:int
    max:int
    

    def init(self, latency:int, sampleCount:int, max:int):
        self.latency = latency
        self.sampleCount = sampleCount
        self.max = max
        
        super().__init__()
    
    