from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class InviteInHavenBagClosedMessage(NetworkMessage):
    hostInformations:'CharacterMinimalInformations'
    

    def init(self, hostInformations:'CharacterMinimalInformations'):
        self.hostInformations = hostInformations
        
        super().__init__()
    
    