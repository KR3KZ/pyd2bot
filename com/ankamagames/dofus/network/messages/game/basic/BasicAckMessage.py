from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicAckMessage(INetworkMessage):
    protocolId = 45
    seq:int
    lastPacketId:int
    
    
