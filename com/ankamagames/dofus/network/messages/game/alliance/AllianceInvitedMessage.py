from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class AllianceInvitedMessage(INetworkMessage):
    protocolId = 6009
    recruterId:int
    recruterName:str
    allianceInfo:BasicNamedAllianceInformations
    
    
