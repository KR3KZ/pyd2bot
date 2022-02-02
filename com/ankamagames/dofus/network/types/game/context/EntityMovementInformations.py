from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class EntityMovementInformations(NetworkMessage):
    id:int
    steps:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    