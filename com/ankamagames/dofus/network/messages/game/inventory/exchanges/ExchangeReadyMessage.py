from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeReadyMessage(NetworkMessage):
    ready:bool
    step:int
    
    
