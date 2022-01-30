from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicAckMessage(INetworkMessage):
    protocolId = 45
    seq:int
    lastPacketId:int
    
    
