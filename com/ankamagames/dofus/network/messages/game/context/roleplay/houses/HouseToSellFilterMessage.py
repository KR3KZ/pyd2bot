from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HouseToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:int
    orderBy:int
    
    
    def __post_init__(self):
        super().__init__()
    