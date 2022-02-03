from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    

    def init(self, channel:int, content:str, timestamp:int, fingerprint:str):
        self.channel = channel
        self.content = content
        self.timestamp = timestamp
        self.fingerprint = fingerprint
        
        super().__init__()
    
    