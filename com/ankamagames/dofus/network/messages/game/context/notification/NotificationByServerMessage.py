from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class NotificationByServerMessage(NetworkMessage):
    id:int
    parameters:list[str]
    forceOpen:bool
    
    
    def __post_init__(self):
        super().__init__()
    