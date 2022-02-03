from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AcquaintanceSearchMessage(NetworkMessage):
    tag:'AccountTagInformation'
    

    def init(self, tag:'AccountTagInformation'):
        self.tag = tag
        
        super().__init__()
    
    