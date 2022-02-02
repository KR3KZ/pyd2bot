from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    state:int
    phenixMapId:int
    
    
    def __post_init__(self):
        super().__init__()
    