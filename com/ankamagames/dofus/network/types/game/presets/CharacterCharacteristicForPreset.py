from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset


@dataclass
class CharacterCharacteristicForPreset(SimpleCharacterCharacteristicForPreset):
    stuff:int
    
    
    def __post_init__(self):
        super().__init__()
    