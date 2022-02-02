from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset


@dataclass
class StatsPreset(Preset):
    stats:list[SimpleCharacterCharacteristicForPreset]
    
    
    def __post_init__(self):
        super().__init__()
    