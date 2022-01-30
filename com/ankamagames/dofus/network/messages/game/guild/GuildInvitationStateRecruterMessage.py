from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationStateRecruterMessage(NetworkMessage):
    protocolId = 5086
    recrutedName:str
    invitationState:int
    
    
