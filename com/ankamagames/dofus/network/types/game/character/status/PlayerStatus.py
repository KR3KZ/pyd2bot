from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PlayerStatus(NetworkMessage):
    statusId:int
    
    
    def __post_init__(self):
        super().__init__()
    