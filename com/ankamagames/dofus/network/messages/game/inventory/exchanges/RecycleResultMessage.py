from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class RecycleResultMessage(NetworkMessage):
    nuggetsForPrism:int
    nuggetsForPlayer:int
    
    
    def __post_init__(self):
        super().__init__()
    