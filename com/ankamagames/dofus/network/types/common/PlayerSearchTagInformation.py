from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
    tag:'AccountTagInformation'
    

    def init(self, tag:'AccountTagInformation'):
        self.tag = tag
        
        super().__init__()
    
    