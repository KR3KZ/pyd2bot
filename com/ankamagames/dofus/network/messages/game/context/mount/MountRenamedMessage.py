from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MountRenamedMessage(NetworkMessage):
    mountId:int
    name:str
    
    
    def __post_init__(self):
        super().__init__()
    