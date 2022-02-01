from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceEndMessage(NetworkMessage):
    actionId:int
    authorId:int
    sequenceType:int
    
    
