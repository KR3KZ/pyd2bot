from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EmoteListMessage(NetworkMessage):
    emoteIds:list[int]
    

    def init(self, emoteIds:list[int]):
        self.emoteIds = emoteIds
        
        super().__init__()
    
    