from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSubareaEmptyInfo(NetworkMessage):
    subAreaId:int
    allianceId:int
    

    def init(self, subAreaId:int, allianceId:int):
        self.subAreaId = subAreaId
        self.allianceId = allianceId
        
        super().__init__()
    
    