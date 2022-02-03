from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
    


class FullStatsPreset(Preset):
    stats:list['CharacterCharacteristicForPreset']
    

    def init(self, stats:list['CharacterCharacteristicForPreset'], id:int):
        self.stats = stats
        
        super().__init__(id)
    
    