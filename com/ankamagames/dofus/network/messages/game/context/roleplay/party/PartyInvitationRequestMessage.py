from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class PartyInvitationRequestMessage(NetworkMessage):
    target:'AbstractPlayerSearchInformation'
    

    def init(self, target:'AbstractPlayerSearchInformation'):
        self.target = target
        
        super().__init__()
    
    