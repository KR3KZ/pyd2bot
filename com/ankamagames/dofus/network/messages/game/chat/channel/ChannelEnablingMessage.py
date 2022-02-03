from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChannelEnablingMessage(NetworkMessage):
    channel:int
    enable:bool
    

    def init(self, channel:int, enable:bool):
        self.channel = channel
        self.enable = enable
        
        super().__init__()
    
    