from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaginationAnswerAbstractMessage(INetworkMessage):
    protocolId = 2864
    offset:int
    count:int
    total:int
    
    
