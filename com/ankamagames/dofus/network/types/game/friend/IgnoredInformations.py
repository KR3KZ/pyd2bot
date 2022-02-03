from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IgnoredInformations(AbstractContactInformations):
    

    def init(self, accountId:int, accountTag:'AccountTagInformation'):
        
        super().__init__(accountId, accountTag)
    
    