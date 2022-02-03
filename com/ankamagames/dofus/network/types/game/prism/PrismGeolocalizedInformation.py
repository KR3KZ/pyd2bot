from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
    


class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    worldX:int
    worldY:int
    mapId:int
    prism:'PrismInformation'
    

    def init(self, worldX:int, worldY:int, mapId:int, prism:'PrismInformation', subAreaId:int, allianceId:int):
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.prism = prism
        
        super().__init__(subAreaId, allianceId)
    
    