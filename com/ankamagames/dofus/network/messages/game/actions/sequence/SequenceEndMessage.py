from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SequenceEndMessage(NetworkMessage):
    actionId:int
    authorId:int
    sequenceType:int
    
    
    def __post_init__(self):
        super().__init__()
    