from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeWeightMessage(NetworkMessage):
    currentWeight:int
    maxWeight:int
    
    
    def __post_init__(self):
        super().__init__()
    