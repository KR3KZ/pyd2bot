from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    


class AllianceInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    allianceInfo:'BasicNamedAllianceInformations'
    

    def init(self, recruterId:int, recruterName:str, allianceInfo:'BasicNamedAllianceInformations'):
        self.recruterId = recruterId
        self.recruterName = recruterName
        self.allianceInfo = allianceInfo
        
        super().__init__()
    
    