from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class InviteInHavenBagOfferMessage(NetworkMessage):
    hostInformations:'CharacterMinimalInformations'
    timeLeftBeforeCancel:int
    

    def init(self, hostInformations:'CharacterMinimalInformations', timeLeftBeforeCancel:int):
        self.hostInformations = hostInformations
        self.timeLeftBeforeCancel = timeLeftBeforeCancel
        
        super().__init__()
    
    