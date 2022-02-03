from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetDeleteRequestMessage(NetworkMessage):
    presetId:int
    

    def init(self, presetId:int):
        self.presetId = presetId
        
        super().__init__()
    
    