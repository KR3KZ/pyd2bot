from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachInvitationRequestMessage(NetworkMessage):
    guests:list[int]
    
    
