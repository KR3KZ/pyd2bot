from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceInvitationAnswerMessage(INetworkMessage):
    protocolId = 6962
    accept:bool
    
    
