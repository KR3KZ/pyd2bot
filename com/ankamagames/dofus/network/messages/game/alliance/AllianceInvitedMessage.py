from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


@dataclass
class AllianceInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    allianceInfo:BasicNamedAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    