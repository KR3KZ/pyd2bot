from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachInvitationCloseMessage(NetworkMessage):
    host:'CharacterMinimalInformations'
    

    def init(self, host:'CharacterMinimalInformations'):
        self.host = host
        
        super().__init__()
    
    