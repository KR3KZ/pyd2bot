from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeReadyMessage(NetworkMessage):
    ready:bool
    step:int
    
    
    def __post_init__(self):
        super().__init__()
    