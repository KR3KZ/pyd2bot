from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HavenBagPackListMessage(NetworkMessage):
    packIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    