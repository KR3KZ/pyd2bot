from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset
    


class SpellsPreset(Preset):
    spells:list['SpellForPreset']
    

    def init(self, spells:list['SpellForPreset'], id:int):
        self.spells = spells
        
        super().__init__(id)
    
    