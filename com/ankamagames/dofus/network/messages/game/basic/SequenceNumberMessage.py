from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SequenceNumberMessage(NetworkMessage):
    protocolId = 1059
    number:int
    
