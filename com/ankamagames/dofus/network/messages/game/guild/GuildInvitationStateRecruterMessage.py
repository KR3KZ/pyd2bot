from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildInvitationStateRecruterMessage(INetworkMessage):
    protocolId = 5086
    recrutedName:str
    invitationState:int
    
    
