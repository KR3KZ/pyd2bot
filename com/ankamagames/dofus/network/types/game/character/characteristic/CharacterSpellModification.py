from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
    


class CharacterSpellModification(NetworkMessage):
    modificationType:int
    spellId:int
    value:'CharacterCharacteristicDetailed'
    

    def init(self, modificationType:int, spellId:int, value:'CharacterCharacteristicDetailed'):
        self.modificationType = modificationType
        self.spellId = spellId
        self.value = value
        
        super().__init__()
    
    