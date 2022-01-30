from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachInvitationAnswerMessage(INetworkMessage):
    protocolId = 5975
    accept:bool
    
    
