from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset


class SpellsPreset(Preset):
    protocolId = 1337
    spells:list[SpellForPreset]
    
