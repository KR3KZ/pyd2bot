from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class PresetsContainerPreset(Preset):
    presets:list['Preset']
    

    def init(self, presets:list['Preset'], id:int):
        self.presets = presets
        
        super().__init__(id)
    
    