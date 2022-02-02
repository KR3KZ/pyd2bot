from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeBuyMessage(NetworkMessage):
    objectToBuyId:int
    quantity:int
    
    
    def __post_init__(self):
        super().__init__()
    