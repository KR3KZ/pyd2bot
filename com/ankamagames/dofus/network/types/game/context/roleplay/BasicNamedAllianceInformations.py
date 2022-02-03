from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


class BasicNamedAllianceInformations(BasicAllianceInformations):
    allianceName:str
    

    def init(self, allianceName:str, allianceId:int, allianceTag:str):
        self.allianceName = allianceName
        
        super().__init__(allianceId, allianceTag)
    
    