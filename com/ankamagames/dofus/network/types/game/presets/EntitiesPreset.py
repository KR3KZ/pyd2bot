from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class EntitiesPreset(Preset):
    iconId:int
    entityIds:list[int]
    

    def init(self, iconId:int, entityIds:list[int], id:int):
        self.iconId = iconId
        self.entityIds = entityIds
        
        super().__init__(id)
    
    