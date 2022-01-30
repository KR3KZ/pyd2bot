from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SequenceStartMessage(NetworkMessage):
    protocolId = 8598
    sequenceType:int
    authorId:float
    
