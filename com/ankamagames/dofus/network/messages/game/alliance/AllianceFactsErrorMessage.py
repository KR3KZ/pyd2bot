from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceFactsErrorMessage(NetworkMessage):
    allianceId:int
    

    def init(self, allianceId:int):
        self.allianceId = allianceId
        
        super().__init__()
    
    