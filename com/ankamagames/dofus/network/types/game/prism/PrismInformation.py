from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInformation(NetworkMessage):
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    

    def init(self, typeId:int, state:int, nextVulnerabilityDate:int, placementDate:int, rewardTokenCount:int):
        self.typeId = typeId
        self.state = state
        self.nextVulnerabilityDate = nextVulnerabilityDate
        self.placementDate = placementDate
        self.rewardTokenCount = rewardTokenCount
        
        super().__init__()
    
    