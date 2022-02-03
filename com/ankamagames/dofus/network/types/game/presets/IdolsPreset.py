from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class IdolsPreset(Preset):
    iconId:int
    idolIds:list[int]
    

    def init(self, iconId:int, idolIds:list[int], id:int):
        self.iconId = iconId
        self.idolIds = idolIds
        
        super().__init__(id)
    
    