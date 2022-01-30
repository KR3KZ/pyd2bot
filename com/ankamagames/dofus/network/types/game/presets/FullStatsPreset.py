from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset


class FullStatsPreset(Preset):
    protocolId = 9471
    stats:list[CharacterCharacteristicForPreset]
    
