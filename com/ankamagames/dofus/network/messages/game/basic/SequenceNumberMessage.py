from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SequenceNumberMessage(INetworkMessage):
    protocolId = 1059
    number:int
    
    
