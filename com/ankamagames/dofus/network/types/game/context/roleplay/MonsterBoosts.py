from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MonsterBoosts(NetworkMessage):
    id:int
    xpBoost:int
    dropBoost:int
    
    
    def __post_init__(self):
        super().__init__()
    