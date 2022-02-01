from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationAnswerAbstractMessage(NetworkMessage):
    offset:int
    count:int
    total:int
    
    
