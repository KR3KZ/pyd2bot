from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildInvitationStateRecrutedMessage(INetworkMessage):
    protocolId = 621
    invitationState:int
    
    
