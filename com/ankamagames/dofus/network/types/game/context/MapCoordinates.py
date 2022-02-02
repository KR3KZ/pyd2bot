from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MapCoordinates(NetworkMessage):
    worldX:int
    worldY:int
    
    
    def __post_init__(self):
        super().__init__()
    