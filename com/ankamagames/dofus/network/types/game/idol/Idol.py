from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class Idol(NetworkMessage):
    id:int
    xpBonusPercent:int
    dropBonusPercent:int
    
    
    def __post_init__(self):
        super().__init__()
    