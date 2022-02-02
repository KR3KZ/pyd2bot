from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightStartingMessage(NetworkMessage):
    fightType:int
    fightId:int
    attackerId:int
    defenderId:int
    containsBoss:bool
    
    
    def __post_init__(self):
        super().__init__()
    