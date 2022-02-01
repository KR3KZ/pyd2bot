from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicAckMessage(NetworkMessage):
    seq:int
    lastPacketId:int
    
    
