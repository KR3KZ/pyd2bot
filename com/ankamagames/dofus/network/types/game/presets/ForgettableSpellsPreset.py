from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.SpellsPreset import SpellsPreset
    from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset
    


class ForgettableSpellsPreset(Preset):
    baseSpellsPreset:'SpellsPreset'
    forgettableSpells:list['SpellForPreset']
    

    def init(self, baseSpellsPreset:'SpellsPreset', forgettableSpells:list['SpellForPreset'], id:int):
        self.baseSpellsPreset = baseSpellsPreset
        self.forgettableSpells = forgettableSpells
        
        super().__init__(id)
    
    