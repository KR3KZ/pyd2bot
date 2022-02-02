from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell


@dataclass
class HouseToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    houseList:list[HouseInformationsForSell]
    
    
    def __post_init__(self):
        super().__init__()
    