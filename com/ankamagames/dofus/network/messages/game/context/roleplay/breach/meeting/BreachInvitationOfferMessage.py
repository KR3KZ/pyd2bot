from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachInvitationOfferMessage(NetworkMessage):
    host:'CharacterMinimalInformations'
    timeLeftBeforeCancel:int
    

    def init(self, host:'CharacterMinimalInformations', timeLeftBeforeCancel:int):
        self.host = host
        self.timeLeftBeforeCancel = timeLeftBeforeCancel
        
        super().__init__()
    
    