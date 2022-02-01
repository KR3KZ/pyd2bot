from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInformation(NetworkMessage):
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    
    
