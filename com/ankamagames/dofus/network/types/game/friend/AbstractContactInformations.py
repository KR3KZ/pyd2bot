from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AbstractContactInformations(NetworkMessage):
    accountId:int
    accountTag:'AccountTagInformation'
    

    def init(self, accountId:int, accountTag:'AccountTagInformation'):
        self.accountId = accountId
        self.accountTag = accountTag
        
        super().__init__()
    
    