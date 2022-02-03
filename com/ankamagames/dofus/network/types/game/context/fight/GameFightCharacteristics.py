from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
    


class GameFightCharacteristics(NetworkMessage):
    characteristics:'CharacterCharacteristics'
    summoner:int
    summoned:bool
    invisibilityState:int
    

    def init(self, characteristics:'CharacterCharacteristics', summoner:int, summoned:bool, invisibilityState:int):
        self.characteristics = characteristics
        self.summoner = summoner
        self.summoned = summoned
        self.invisibilityState = invisibilityState
        
        super().__init__()
    
    