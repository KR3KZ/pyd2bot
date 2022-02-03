from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IconPresetSaveRequestMessage(NetworkMessage):
    presetId:int
    symbolId:int
    updateData:bool
    

    def init(self, presetId:int, symbolId:int, updateData:bool):
        self.presetId = presetId
        self.symbolId = symbolId
        self.updateData = updateData
        
        super().__init__()
    
    