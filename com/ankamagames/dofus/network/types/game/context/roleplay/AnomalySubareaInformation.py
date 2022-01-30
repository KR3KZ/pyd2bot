from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AnomalySubareaInformation(NetworkMessage):
    protocolId = 8338
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    
