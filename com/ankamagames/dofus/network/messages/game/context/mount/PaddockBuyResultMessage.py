from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PaddockBuyResultMessage(NetworkMessage):
    paddockId:int
    bought:bool
    realPrice:int
    
    
    def __post_init__(self):
        super().__init__()
    