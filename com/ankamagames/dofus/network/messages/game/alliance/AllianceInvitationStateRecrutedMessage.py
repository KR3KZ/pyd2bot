from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceInvitationStateRecrutedMessage(INetworkMessage):
    protocolId = 7918
    invitationState:int
    
    
