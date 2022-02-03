from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
    


class StatsPreset(Preset):
    stats:list['SimpleCharacterCharacteristicForPreset']
    

    def init(self, stats:list['SimpleCharacterCharacteristicForPreset'], id:int):
        self.stats = stats
        
        super().__init__(id)
    
    