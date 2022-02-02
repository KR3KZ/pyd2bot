from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SpouseStatusMessage(NetworkMessage):
    hasSpouse:bool
    
    
    def __post_init__(self):
        super().__init__()
    