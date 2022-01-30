from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaginationAnswerAbstractMessage(NetworkMessage):
    protocolId = 2864
    offset:float
    count:int
    total:int
    
