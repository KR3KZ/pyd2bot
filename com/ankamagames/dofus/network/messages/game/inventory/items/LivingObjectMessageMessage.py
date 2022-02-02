from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class LivingObjectMessageMessage(NetworkMessage):
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    
    
    def __post_init__(self):
        super().__init__()
    