from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.SpellsPreset import SpellsPreset
from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset


@dataclass
class ForgettableSpellsPreset(Preset):
    baseSpellsPreset:SpellsPreset
    forgettableSpells:list[SpellForPreset]
    
    
    def __post_init__(self):
        super().__init__()
    