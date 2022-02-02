from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ObjectGroundListAddedMessage(NetworkMessage):
    cells:list[int]
    referenceIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    