from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


@dataclass
class HousePropertiesMessage(NetworkMessage):
    houseId:int
    doorsOnMap:list[int]
    properties:HouseInstanceInformations
    
    
    def __post_init__(self):
        super().__init__()
    