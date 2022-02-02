from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class BasicLatencyStatsMessage(NetworkMessage):
    latency:int
    sampleCount:int
    max:int
    
    
    def __post_init__(self):
        super().__init__()
    