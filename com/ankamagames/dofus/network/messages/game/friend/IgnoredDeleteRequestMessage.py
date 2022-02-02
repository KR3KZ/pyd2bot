from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class IgnoredDeleteRequestMessage(NetworkMessage):
    accountId:int
    session:bool
    
    
    def __post_init__(self):
        super().__init__()
    