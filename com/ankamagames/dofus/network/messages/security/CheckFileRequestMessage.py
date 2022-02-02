from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CheckFileRequestMessage(NetworkMessage):
    filename:str
    type:int
    
    
    def __post_init__(self):
        super().__init__()
    