from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectRequestMessage(NetworkMessage):
    idolId:int
    activate:bool
    party:bool
    
    
