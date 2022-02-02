from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PaginationAnswerAbstractMessage(NetworkMessage):
    offset:int
    count:int
    total:int
    
    
    def __post_init__(self):
        super().__init__()
    