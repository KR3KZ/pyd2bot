from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    name:str
    type:int
    

    def init(self, name:str, type:int, presetId:int, symbolId:int, updateData:bool):
        self.name = name
        self.type = type
        
        super().__init__(presetId, symbolId, updateData)
    
    