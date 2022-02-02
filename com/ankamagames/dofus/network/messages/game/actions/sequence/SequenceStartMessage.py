from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SequenceStartMessage(NetworkMessage):
    sequenceType:int
    authorId:int
    
    
    def __post_init__(self):
        super().__init__()
    