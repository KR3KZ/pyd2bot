from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    targetId:int
    targetCellId:int
    friendly:bool
    
    
    def __post_init__(self):
        super().__init__()
    