from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaginationRequestAbstractMessage(INetworkMessage):
    protocolId = 789
    offset:int
    count:int
    
    
