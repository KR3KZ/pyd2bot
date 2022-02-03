from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicAllianceInformations(AbstractSocialGroupInfos):
    allianceId:int
    allianceTag:str
    

    def init(self, allianceId:int, allianceTag:str):
        self.allianceId = allianceId
        self.allianceTag = allianceTag
        
        super().__init__()
    
    