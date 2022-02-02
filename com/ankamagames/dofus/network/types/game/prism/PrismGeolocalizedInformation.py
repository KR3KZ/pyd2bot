from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation


@dataclass
class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    worldX:int
    worldY:int
    mapId:int
    prism:PrismInformation
    
    
    def __post_init__(self):
        super().__init__()
    