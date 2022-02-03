from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo
    


class DecraftResultMessage(NetworkMessage):
    results:list['DecraftedItemStackInfo']
    

    def init(self, results:list['DecraftedItemStackInfo']):
        self.results = results
        
        super().__init__()
    
    