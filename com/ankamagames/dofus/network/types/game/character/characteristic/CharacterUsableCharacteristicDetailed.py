from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


@dataclass
class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
    used:int
    
    
    def __post_init__(self):
        super().__init__()
    