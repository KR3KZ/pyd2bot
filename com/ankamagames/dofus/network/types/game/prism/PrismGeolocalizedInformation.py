from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation


class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    worldX:int
    worldY:int
    mapId:int
    prism:PrismInformation
    
    
