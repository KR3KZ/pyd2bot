from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeStartOkRecycleTradeMessage(NetworkMessage):
    percentToPrism:int
    percentToPlayer:int
    
    
    def __post_init__(self):
        super().__init__()
    