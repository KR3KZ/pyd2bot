from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportDestination(NetworkMessage):
    type:int
    mapId:int
    subAreaId:int
    level:int
    cost:int
    
    
    def __post_init__(self):
        super().__init__()
    