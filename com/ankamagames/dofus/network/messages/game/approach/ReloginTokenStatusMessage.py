from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ReloginTokenStatusMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    
    
