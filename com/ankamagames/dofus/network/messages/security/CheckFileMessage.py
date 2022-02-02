from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CheckFileMessage(NetworkMessage):
    filenameHash:str
    type:int
    value:str
    
    
    def __post_init__(self):
        super().__init__()
    