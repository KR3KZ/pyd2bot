from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightTurnEndMessage(NetworkMessage):
    id:int
    
    
    def __post_init__(self):
        super().__init__()
    