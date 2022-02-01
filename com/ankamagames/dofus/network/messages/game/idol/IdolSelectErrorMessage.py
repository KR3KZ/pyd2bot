from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectErrorMessage(NetworkMessage):
    reason:int
    idolId:int
    activate:bool
    party:bool
    
    
