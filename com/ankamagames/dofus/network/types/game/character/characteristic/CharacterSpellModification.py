from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


@dataclass
class CharacterSpellModification(NetworkMessage):
    modificationType:int
    spellId:int
    value:CharacterCharacteristicDetailed
    
    
    def __post_init__(self):
        super().__init__()
    