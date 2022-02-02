from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class QueueStatusMessage(NetworkMessage):
    position:int
    total:int
    
    
    def __post_init__(self):
        super().__init__()
    