from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class FightStartingPositions(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    