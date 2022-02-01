from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachInvitationRequestMessage(INetworkMessage):
    protocolId = 7544
    guests:int
    
    
