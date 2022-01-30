from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SequenceEndMessage(INetworkMessage):
    protocolId = 5912
    actionId:int
    authorId:int
    sequenceType:int
    
    
