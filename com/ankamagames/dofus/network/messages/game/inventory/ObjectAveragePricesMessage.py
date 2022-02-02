from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ObjectAveragePricesMessage(NetworkMessage):
    ids:list[int]
    avgPrices:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    