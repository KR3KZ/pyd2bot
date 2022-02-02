from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ObjectMovementMessage(NetworkMessage):
    objectUID:int
    position:int
    
    
    def __post_init__(self):
        super().__init__()
    