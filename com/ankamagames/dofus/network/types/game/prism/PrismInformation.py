from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismInformation(INetworkMessage):
    protocolId = 6060
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    
    
