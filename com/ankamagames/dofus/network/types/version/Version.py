from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class Version(NetworkMessage):
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    
    
    def __post_init__(self):
        super().__init__()
    