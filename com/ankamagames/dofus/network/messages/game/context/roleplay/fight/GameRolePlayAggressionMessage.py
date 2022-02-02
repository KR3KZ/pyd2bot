from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayAggressionMessage(NetworkMessage):
    attackerId:int
    defenderId:int
    
    
    def __post_init__(self):
        super().__init__()
    