from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class JobCrafterDirectorySettings(NetworkMessage):
    jobId:int
    minLevel:int
    free:bool
    
    
    def __post_init__(self):
        super().__init__()
    