from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachInvitationResponseMessage(NetworkMessage):
    guest:'CharacterMinimalInformations'
    accept:bool
    

    def init(self, guest:'CharacterMinimalInformations', accept:bool):
        self.guest = guest
        self.accept = accept
        
        super().__init__()
    
    