from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalySubareaInformation(NetworkMessage):
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    
    
