from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    teamNumber:int
    
    
    def __post_init__(self):
        super().__init__()
    