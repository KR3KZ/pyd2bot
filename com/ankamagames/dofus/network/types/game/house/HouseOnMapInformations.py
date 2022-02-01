from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class HouseOnMapInformations(HouseInformations):
    doorsOnMap:list[int]
    houseInstances:list[HouseInstanceInformations]
    
    
