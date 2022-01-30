from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationStateRecrutedMessage(NetworkMessage):
    protocolId = 621
    invitationState:int
    
    
