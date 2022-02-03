from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InvalidPresetsMessage(NetworkMessage):
    presetIds:list[int]
    

    def init(self, presetIds:list[int]):
        self.presetIds = presetIds
        
        super().__init__()
    
    