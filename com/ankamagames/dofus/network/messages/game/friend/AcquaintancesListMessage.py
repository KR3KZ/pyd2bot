from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
    


class AcquaintancesListMessage(NetworkMessage):
    acquaintanceList:list['AcquaintanceInformation']
    

    def init(self, acquaintanceList:list['AcquaintanceInformation']):
        self.acquaintanceList = acquaintanceList
        
        super().__init__()
    
    