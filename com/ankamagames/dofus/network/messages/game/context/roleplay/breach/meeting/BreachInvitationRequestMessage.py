from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationRequestMessage(NetworkMessage):
    protocolId = 7544
    guests:int
    
    
