from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceInvitationStateRecrutedMessage(INetworkMessage):
    protocolId = 7918
    invitationState:int
    
    
