from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class EntityInformation(NetworkMessage):
    id:int
    experience:int
    status:bool
    
    
    def __post_init__(self):
        super().__init__()
    