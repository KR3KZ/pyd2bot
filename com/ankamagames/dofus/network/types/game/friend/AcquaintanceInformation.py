from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AcquaintanceInformation(AbstractContactInformations):
    playerState:int
    

    def init(self, playerState:int, accountId:int, accountTag:'AccountTagInformation'):
        self.playerState = playerState
        
        super().__init__(accountId, accountTag)
    
    