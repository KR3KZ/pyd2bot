from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RawDataMessage(NetworkMessage):
    content:bytearray
    

    def init(self, content:bytearray):
        self.content = content
        
        super().__init__()
    
    