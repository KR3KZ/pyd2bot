from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceModificationNameAndTagValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    

    def init(self, allianceName:str, allianceTag:str):
        self.allianceName = allianceName
        self.allianceTag = allianceTag
        
        super().__init__()
    
    