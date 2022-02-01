from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInvitationStateRecruterMessage(NetworkMessage):
    recrutedName:str
    invitationState:int
    
    
