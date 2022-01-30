from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecrutedMessage(NetworkMessage):
    protocolId = 7918
    invitationState:int
    
