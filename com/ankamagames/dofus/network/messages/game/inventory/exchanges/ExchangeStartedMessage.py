from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeStartedMessage(NetworkMessage):
    exchangeType:int
    
    
    def __post_init__(self):
        super().__init__()
    