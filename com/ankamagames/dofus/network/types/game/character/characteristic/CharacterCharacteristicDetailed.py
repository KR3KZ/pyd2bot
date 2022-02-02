from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


@dataclass
class CharacterCharacteristicDetailed(CharacterCharacteristic):
    base:int
    additional:int
    objectsAndMountBonus:int
    alignGiftBonus:int
    contextModif:int
    
    
    def __post_init__(self):
        super().__init__()
    