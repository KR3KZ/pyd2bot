from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class IdolSelectRequestMessage(NetworkMessage):
    idolId:int
    activate:bool
    party:bool
    
    
    def __post_init__(self):
        super().__init__()
    