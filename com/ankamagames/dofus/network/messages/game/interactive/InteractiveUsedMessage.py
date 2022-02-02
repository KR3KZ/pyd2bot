from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class InteractiveUsedMessage(NetworkMessage):
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    
    
    def __post_init__(self):
        super().__init__()
    