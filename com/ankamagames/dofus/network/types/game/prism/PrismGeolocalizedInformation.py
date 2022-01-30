from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation


class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    protocolId = 2406
    worldX:int
    worldY:int
    mapId:float
    prism:PrismInformation
    
