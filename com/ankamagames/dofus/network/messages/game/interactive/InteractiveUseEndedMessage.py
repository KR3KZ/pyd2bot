from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class InteractiveUseEndedMessage(NetworkMessage):
    elemId:int
    skillId:int
    
    
    def __post_init__(self):
        super().__init__()
    