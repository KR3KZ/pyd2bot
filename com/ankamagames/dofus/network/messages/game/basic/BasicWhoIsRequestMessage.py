from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class BasicWhoIsRequestMessage(NetworkMessage):
    verbose:bool
    target:'AbstractPlayerSearchInformation'
    

    def init(self, verbose:bool, target:'AbstractPlayerSearchInformation'):
        self.verbose = verbose
        self.target = target
        
        super().__init__()
    
    