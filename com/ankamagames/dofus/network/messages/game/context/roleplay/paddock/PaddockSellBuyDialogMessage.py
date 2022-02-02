from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PaddockSellBuyDialogMessage(NetworkMessage):
    bsell:bool
    ownerId:int
    price:int
    
    
    def __post_init__(self):
        super().__init__()
    