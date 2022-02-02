from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AchievementObjective(NetworkMessage):
    id:int
    maxValue:int
    
    
    def __post_init__(self):
        super().__init__()
    