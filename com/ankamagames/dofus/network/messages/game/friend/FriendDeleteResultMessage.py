from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendDeleteResultMessage(NetworkMessage):
    success:bool
    tag:'AccountTagInformation'
    

    def init(self, success:bool, tag:'AccountTagInformation'):
        self.success = success
        self.tag = tag
        
        super().__init__()
    
    