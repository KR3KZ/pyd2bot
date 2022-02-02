from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HavenBagPermissionsUpdateMessage(NetworkMessage):
    permissions:int
    
    
    def __post_init__(self):
        super().__init__()
    