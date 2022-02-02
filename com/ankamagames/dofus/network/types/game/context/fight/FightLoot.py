from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class FightLoot(NetworkMessage):
    objects:list[int]
    kamas:int
    
    
    def __post_init__(self):
        super().__init__()
    