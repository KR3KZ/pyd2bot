from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildInvitationStateRecruterMessage(INetworkMessage):
    protocolId = 5086
    recrutedName:str
    invitationState:int
    
    
