from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachKickResponseMessage(NetworkMessage):
    target:'CharacterMinimalInformations'
    kicked:bool
    

    def init(self, target:'CharacterMinimalInformations', kicked:bool):
        self.target = target
        self.kicked = kicked
        
        super().__init__()
    
    