from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class DungeonKeyRingUpdateMessage(NetworkMessage):
    dungeonId:int
    available:bool
    
    
    def __post_init__(self):
        super().__init__()
    