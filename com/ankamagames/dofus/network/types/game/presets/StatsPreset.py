from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset


class StatsPreset(Preset):
    protocolId = 6559
    stats:SimpleCharacterCharacteristicForPreset
    
