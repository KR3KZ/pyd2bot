from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class JobCrafterDirectoryEntryJobInfo(NetworkMessage):
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    