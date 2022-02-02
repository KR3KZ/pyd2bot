from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


@dataclass
class AccountHouseInformations(HouseInformations):
    houseInfos:HouseInstanceInformations
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
    def __post_init__(self):
        super().__init__()
    