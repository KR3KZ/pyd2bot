from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceInvitationStateRecruterMessage(INetworkMessage):
    protocolId = 2498
    recrutedName:str
    invitationState:int
    
    
