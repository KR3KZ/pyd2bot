from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildInvitationStateRecrutedMessage(INetworkMessage):
    protocolId = 621
    invitationState:int
    
    
