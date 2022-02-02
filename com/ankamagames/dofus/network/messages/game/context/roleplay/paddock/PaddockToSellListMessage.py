from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell


@dataclass
class PaddockToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    paddockList:list[PaddockInformationsForSell]
    
    
    def __post_init__(self):
        super().__init__()
    