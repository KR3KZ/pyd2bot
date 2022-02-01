from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildInvitationAnswerMessage(INetworkMessage):
    protocolId = 8895
    accept:bool
    
    
