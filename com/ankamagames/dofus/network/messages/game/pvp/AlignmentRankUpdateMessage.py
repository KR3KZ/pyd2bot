from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AlignmentRankUpdateMessage(NetworkMessage):
    alignmentRank:int
    verbose:bool
    
    
    def __post_init__(self):
        super().__init__()
    