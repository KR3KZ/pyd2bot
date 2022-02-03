from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
    


class HousePropertiesMessage(NetworkMessage):
    houseId:int
    doorsOnMap:list[int]
    properties:'HouseInstanceInformations'
    

    def init(self, houseId:int, doorsOnMap:list[int], properties:'HouseInstanceInformations'):
        self.houseId = houseId
        self.doorsOnMap = doorsOnMap
        self.properties = properties
        
        super().__init__()
    
    