from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecruterMessage(NetworkMessage):
    protocolId = 2498
    recrutedName:str
    invitationState:int
    
