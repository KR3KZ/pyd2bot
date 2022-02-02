from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


@dataclass
class CharacterCharacteristics(NetworkMessage):
    characteristics:list[CharacterCharacteristic]
    
    
    def __post_init__(self):
        super().__init__()
    