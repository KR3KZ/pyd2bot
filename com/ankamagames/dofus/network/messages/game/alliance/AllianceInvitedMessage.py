from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class AllianceInvitedMessage(NetworkMessage):
    protocolId = 6009
    recruterId:float
    recruterName:str
    allianceInfo:BasicNamedAllianceInformations
    
