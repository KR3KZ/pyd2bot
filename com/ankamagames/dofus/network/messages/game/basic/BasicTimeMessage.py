from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicTimeMessage(NetworkMessage):
    timestamp:int
    timezoneOffset:int
    

    def init(self, timestamp:int, timezoneOffset:int):
        self.timestamp = timestamp
        self.timezoneOffset = timezoneOffset
        
        super().__init__()
    
    