from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ActivityLockRequestMessage(NetworkMessage):
    activityId:int
    lock:bool
    
    
    def __post_init__(self):
        super().__init__()
    