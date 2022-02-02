from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TrustStatusMessage(NetworkMessage):
    trusted:bool
    certified:bool
    
    
    def __post_init__(self):
        super().__init__()
    