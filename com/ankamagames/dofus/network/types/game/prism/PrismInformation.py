from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismInformation(INetworkMessage):
    protocolId = 6060
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    
    
