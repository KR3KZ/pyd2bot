from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SequenceEndMessage(INetworkMessage):
    protocolId = 5912
    actionId:int
    authorId:int
    sequenceType:int
    
    
