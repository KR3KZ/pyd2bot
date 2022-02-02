from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightTurnFinishMessage(NetworkMessage):
    isAfk:bool
    
    
    def __post_init__(self):
        super().__init__()
    