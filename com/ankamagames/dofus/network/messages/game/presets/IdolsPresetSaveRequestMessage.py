from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IdolsPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    

    def init(self, presetId:int, symbolId:int, updateData:bool):
        
        super().__init__(presetId, symbolId, updateData)
    
    