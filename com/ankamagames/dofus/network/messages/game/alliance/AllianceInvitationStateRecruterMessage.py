from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceInvitationStateRecruterMessage(INetworkMessage):
    protocolId = 2498
    recrutedName:str
    invitationState:int
    
    
