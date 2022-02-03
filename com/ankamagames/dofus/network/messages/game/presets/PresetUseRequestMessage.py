from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetUseRequestMessage(NetworkMessage):
    presetId:int
    

    def init(self, presetId:int):
        self.presetId = presetId
        
        super().__init__()
    
    