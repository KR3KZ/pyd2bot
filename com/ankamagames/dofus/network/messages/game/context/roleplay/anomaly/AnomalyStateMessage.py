from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    subAreaId:int
    open:bool
    closingTime:int
    
    
