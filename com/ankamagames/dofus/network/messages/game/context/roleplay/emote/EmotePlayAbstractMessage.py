from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EmotePlayAbstractMessage(NetworkMessage):
    emoteId:int
    emoteStartTime:int
    

    def init(self, emoteId:int, emoteStartTime:int):
        self.emoteId = emoteId
        self.emoteStartTime = emoteStartTime
        
        super().__init__()
    
    