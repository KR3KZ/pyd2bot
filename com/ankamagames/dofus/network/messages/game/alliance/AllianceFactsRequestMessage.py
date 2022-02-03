from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceFactsRequestMessage(NetworkMessage):
    allianceId:int
    

    def init(self, allianceId:int):
        self.allianceId = allianceId
        
        super().__init__()
    
    