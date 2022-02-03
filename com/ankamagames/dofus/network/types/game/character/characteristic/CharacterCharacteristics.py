from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
    


class CharacterCharacteristics(NetworkMessage):
    characteristics:list['CharacterCharacteristic']
    

    def init(self, characteristics:list['CharacterCharacteristic']):
        self.characteristics = characteristics
        
        super().__init__()
    
    