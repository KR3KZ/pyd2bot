from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
    


class PaddockInstancesInformations(PaddockInformations):
    paddocks:list['PaddockBuyableInformations']
    

    def init(self, paddocks:list['PaddockBuyableInformations'], maxOutdoorMount:int, maxItems:int):
        self.paddocks = paddocks
        
        super().__init__(maxOutdoorMount, maxItems)
    
    