from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TrustCertificate(NetworkMessage):
    id:int
    hash:str
    
    
    def __post_init__(self):
        super().__init__()
    