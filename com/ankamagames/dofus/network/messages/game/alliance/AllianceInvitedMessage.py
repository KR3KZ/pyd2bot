from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class AllianceInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    allianceInfo:BasicNamedAllianceInformations
    
    
