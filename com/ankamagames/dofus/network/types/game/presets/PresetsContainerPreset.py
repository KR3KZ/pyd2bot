from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


@dataclass
class PresetsContainerPreset(Preset):
    presets:list[Preset]
    
    
    def __post_init__(self):
        super().__init__()
    