from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AnomalySubareaInformation(INetworkMessage):
    protocolId = 8338
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    
    
