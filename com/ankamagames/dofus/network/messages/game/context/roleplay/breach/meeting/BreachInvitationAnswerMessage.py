from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachInvitationAnswerMessage(INetworkMessage):
    protocolId = 5975
    accept:bool
    
    
