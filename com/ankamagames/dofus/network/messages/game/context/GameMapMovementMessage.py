from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameMapMovementMessage(NetworkMessage):
    keyMovements:list[int]
    forcedDirection:int
    actorId:int
    
    
    def __post_init__(self):
        super().__init__()
    