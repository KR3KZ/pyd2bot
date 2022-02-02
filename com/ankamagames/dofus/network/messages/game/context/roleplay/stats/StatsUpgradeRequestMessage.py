from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class StatsUpgradeRequestMessage(NetworkMessage):
    useAdditionnal:bool
    statId:int
    boostPoint:int
    
    
    def __post_init__(self):
        super().__init__()
    