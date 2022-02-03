from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    channels:list[int]
    disallowed:list[int]
    

    def init(self, channels:list[int], disallowed:list[int]):
        self.channels = channels
        self.disallowed = disallowed
        
        super().__init__()
    
    