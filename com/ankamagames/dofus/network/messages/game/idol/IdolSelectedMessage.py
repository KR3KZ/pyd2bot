from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectedMessage(NetworkMessage):
    idolId:int
    activate:bool
    party:bool
    
    
