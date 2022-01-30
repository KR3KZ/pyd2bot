from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicAckMessage(NetworkMessage):
    protocolId = 45
    seq:int
    lastPacketId:int
    
    
