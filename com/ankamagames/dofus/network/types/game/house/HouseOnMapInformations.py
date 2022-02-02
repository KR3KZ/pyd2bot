from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


@dataclass
class HouseOnMapInformations(HouseInformations):
    doorsOnMap:list[int]
    houseInstances:list[HouseInstanceInformations]
    
    
    def __post_init__(self):
        super().__init__()
    