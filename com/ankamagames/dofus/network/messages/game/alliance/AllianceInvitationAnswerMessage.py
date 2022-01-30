from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceInvitationAnswerMessage(INetworkMessage):
    protocolId = 6962
    accept:bool
    
    
