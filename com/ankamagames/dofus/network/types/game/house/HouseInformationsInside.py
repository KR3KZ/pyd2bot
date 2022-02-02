from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


@dataclass
class HouseInformationsInside(HouseInformations):
    houseInfos:HouseInstanceInformations
    worldX:int
    worldY:int
    
    
    def __post_init__(self):
        super().__init__()
    