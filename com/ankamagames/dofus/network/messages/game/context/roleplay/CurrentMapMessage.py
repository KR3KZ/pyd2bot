from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CurrentMapMessage(NetworkMessage):
    mapId:int
    mapKey:str
    
    
    def __post_init__(self):
        super().__init__()
    