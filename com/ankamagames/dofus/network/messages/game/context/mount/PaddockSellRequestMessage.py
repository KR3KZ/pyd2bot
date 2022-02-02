from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PaddockSellRequestMessage(NetworkMessage):
    price:int
    forSale:bool
    
    
    def __post_init__(self):
        super().__init__()
    