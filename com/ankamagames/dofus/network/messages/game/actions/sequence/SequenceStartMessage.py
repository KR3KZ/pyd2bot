from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SequenceStartMessage(INetworkMessage):
    protocolId = 8598
    sequenceType:int
    authorId:int
    
    
