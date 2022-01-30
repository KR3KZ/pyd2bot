from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildInvitationAnswerMessage(INetworkMessage):
    protocolId = 8895
    accept:bool
    
    
