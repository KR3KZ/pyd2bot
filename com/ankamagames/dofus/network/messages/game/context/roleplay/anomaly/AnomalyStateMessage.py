from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AnomalyStateMessage(NetworkMessage):
    subAreaId:int
    open:bool
    closingTime:int
    
    
    def __post_init__(self):
        super().__init__()
    