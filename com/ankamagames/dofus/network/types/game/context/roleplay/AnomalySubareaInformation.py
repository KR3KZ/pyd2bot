from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalySubareaInformation(NetworkMessage):
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    

    def init(self, subAreaId:int, rewardRate:int, hasAnomaly:bool, anomalyClosingTime:int):
        self.subAreaId = subAreaId
        self.rewardRate = rewardRate
        self.hasAnomaly = hasAnomaly
        self.anomalyClosingTime = anomalyClosingTime
        
        super().__init__()
    
    