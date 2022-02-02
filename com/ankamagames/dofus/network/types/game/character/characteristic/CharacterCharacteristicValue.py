from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


@dataclass
class CharacterCharacteristicValue(CharacterCharacteristic):
    total:int
    
    
    def __post_init__(self):
        super().__init__()
    