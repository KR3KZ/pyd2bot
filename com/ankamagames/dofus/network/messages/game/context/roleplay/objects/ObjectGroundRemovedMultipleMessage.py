from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ObjectGroundRemovedMultipleMessage(NetworkMessage):
    cells:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    