from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SequenceStartMessage(INetworkMessage):
    protocolId = 8598
    sequenceType:int
    authorId:int
    
    
