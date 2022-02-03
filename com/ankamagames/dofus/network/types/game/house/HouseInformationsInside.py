from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
    


class HouseInformationsInside(HouseInformations):
    houseInfos:'HouseInstanceInformations'
    worldX:int
    worldY:int
    

    def init(self, houseInfos:'HouseInstanceInformations', worldX:int, worldY:int, houseId:int, modelId:int):
        self.houseInfos = houseInfos
        self.worldX = worldX
        self.worldY = worldY
        
        super().__init__(houseId, modelId)
    
    