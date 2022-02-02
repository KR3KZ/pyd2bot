from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ChangeMapMessage(NetworkMessage):
    mapId:int
    autopilot:bool
    
    
    def __post_init__(self):
        super().__init__()
    