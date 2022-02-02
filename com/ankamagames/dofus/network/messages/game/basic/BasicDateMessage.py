from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class BasicDateMessage(NetworkMessage):
    day:int
    month:int
    year:int
    
    
    def __post_init__(self):
        super().__init__()
    