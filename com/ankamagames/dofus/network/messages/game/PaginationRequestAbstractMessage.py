from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationRequestAbstractMessage(NetworkMessage):
    offset:int
    count:int
    
    
