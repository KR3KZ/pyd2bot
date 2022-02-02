from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations


@dataclass
class PaddockInstancesInformations(PaddockInformations):
    paddocks:list[PaddockBuyableInformations]
    
    
    def __post_init__(self):
        super().__init__()
    