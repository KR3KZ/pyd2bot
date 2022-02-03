from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicAckMessage(NetworkMessage):
    seq:int
    lastPacketId:int
    

    def init(self, seq:int, lastPacketId:int):
        self.seq = seq
        self.lastPacketId = lastPacketId
        
        super().__init__()
    
    