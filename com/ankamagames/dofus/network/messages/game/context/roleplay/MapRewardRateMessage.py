from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MapRewardRateMessage(NetworkMessage):
    mapRate:int
    subAreaRate:int
    totalRate:int
    
    
    def __post_init__(self):
        super().__init__()
    