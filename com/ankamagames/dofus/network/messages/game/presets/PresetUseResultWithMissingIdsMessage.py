from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import PresetUseResultMessage


class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    missingIds:list[int]
    

    def init(self, missingIds:list[int], presetId:int, code:int):
        self.missingIds = missingIds
        
        super().__init__(presetId, code)
    
    