from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SystemMessageDisplayMessage(NetworkMessage):
    hangUp:bool
    msgId:int
    parameters:list[str]
    
    
    def __post_init__(self):
        super().__init__()
    