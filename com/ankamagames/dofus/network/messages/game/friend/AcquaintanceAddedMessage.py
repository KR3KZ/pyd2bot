from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
    


class AcquaintanceAddedMessage(NetworkMessage):
    acquaintanceAdded:'AcquaintanceInformation'
    

    def init(self, acquaintanceAdded:'AcquaintanceInformation'):
        self.acquaintanceAdded = acquaintanceAdded
        
        super().__init__()
    
    