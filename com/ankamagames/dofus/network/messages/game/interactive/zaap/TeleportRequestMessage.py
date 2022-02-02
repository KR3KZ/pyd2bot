from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportRequestMessage(NetworkMessage):
    sourceType:int
    destinationType:int
    mapId:int
    
    
    def __post_init__(self):
        super().__init__()
    