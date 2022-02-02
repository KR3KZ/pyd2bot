from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    skinId:int
    
    
    def __post_init__(self):
        super().__init__()
    