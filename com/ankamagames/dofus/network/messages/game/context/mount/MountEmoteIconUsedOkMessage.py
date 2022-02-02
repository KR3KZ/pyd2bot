from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MountEmoteIconUsedOkMessage(NetworkMessage):
    mountId:int
    reactionType:int
    
    
    def __post_init__(self):
        super().__init__()
    