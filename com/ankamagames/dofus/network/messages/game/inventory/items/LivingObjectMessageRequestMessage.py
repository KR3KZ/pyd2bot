from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class LivingObjectMessageRequestMessage(NetworkMessage):
    msgId:int
    parameters:list[str]
    livingObject:int
    
    
    def __post_init__(self):
        super().__init__()
    