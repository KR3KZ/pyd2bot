from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceStartMessage(NetworkMessage):
    sequenceType:int
    authorId:int
    
    
