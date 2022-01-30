from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationAnswerMessage(NetworkMessage):
    protocolId = 6962
    accept:bool
    
