from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaginationRequestAbstractMessage(INetworkMessage):
    protocolId = 789
    offset:int
    count:int
    
    
