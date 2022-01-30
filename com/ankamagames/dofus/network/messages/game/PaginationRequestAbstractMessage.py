from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaginationRequestAbstractMessage(NetworkMessage):
    protocolId = 789
    offset:float
    count:int
    
