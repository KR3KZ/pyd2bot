from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset


@dataclass
class SpellsPreset(Preset):
    spells:list[SpellForPreset]
    
    
    def __post_init__(self):
        super().__init__()
    