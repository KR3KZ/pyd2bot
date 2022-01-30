from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationAnswerMessage(NetworkMessage):
    protocolId = 5975
    accept:bool
    
    
