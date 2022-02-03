from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
    


class HouseOnMapInformations(HouseInformations):
    doorsOnMap:list[int]
    houseInstances:list['HouseInstanceInformations']
    

    def init(self, doorsOnMap:list[int], houseInstances:list['HouseInstanceInformations'], houseId:int, modelId:int):
        self.doorsOnMap = doorsOnMap
        self.houseInstances = houseInstances
        
        super().__init__(houseId, modelId)
    
    