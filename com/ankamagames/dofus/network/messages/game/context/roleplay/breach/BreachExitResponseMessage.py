from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class BreachExitResponseMessage(NetworkMessage):
    exited:bool
    
    
    def __post_init__(self):
        super().__init__()
    