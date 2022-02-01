from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorStateUpdateMessage(NetworkMessage):
    uniqueId:int
    state:int
    
    
