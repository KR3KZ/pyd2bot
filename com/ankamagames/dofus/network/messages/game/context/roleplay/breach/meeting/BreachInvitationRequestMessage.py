from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachInvitationRequestMessage(INetworkMessage):
    protocolId = 7544
    guests:int
    
    
