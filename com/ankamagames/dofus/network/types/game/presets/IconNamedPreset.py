from com.ankamagames.dofus.network.types.game.presets.PresetsContainerPreset import PresetsContainerPreset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class IconNamedPreset(PresetsContainerPreset):
    iconId:int
    name:str
    

    def init(self, iconId:int, name:str, presets:list['Preset'], id:int):
        self.iconId = iconId
        self.name = name
        
        super().__init__(presets, id)
    
    