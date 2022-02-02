from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TitlesAndOrnamentsListMessage(NetworkMessage):
    titles:list[int]
    ornaments:list[int]
    activeTitle:int
    activeOrnament:int
    
    
    def __post_init__(self):
        super().__init__()
    