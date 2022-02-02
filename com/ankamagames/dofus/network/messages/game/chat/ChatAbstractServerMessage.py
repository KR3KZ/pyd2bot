from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ChatAbstractServerMessage(NetworkMessage):
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    
    
    def __post_init__(self):
        super().__init__()
    