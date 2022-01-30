from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismInformation(NetworkMessage):
    protocolId = 6060
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    
    
