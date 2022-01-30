from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SequenceEndMessage(NetworkMessage):
    protocolId = 5912
    actionId:int
    authorId:int
    sequenceType:int
    
