from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TreasureHuntFinishedMessage(NetworkMessage):
    questType:int
    
    
    def __post_init__(self):
        super().__init__()
    