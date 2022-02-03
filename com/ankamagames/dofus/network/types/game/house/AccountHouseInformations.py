from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
    


class AccountHouseInformations(HouseInformations):
    houseInfos:'HouseInstanceInformations'
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    

    def init(self, houseInfos:'HouseInstanceInformations', worldX:int, worldY:int, mapId:int, subAreaId:int, houseId:int, modelId:int):
        self.houseInfos = houseInfos
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        
        super().__init__(houseId, modelId)
    
    