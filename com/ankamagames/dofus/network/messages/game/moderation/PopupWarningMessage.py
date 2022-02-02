from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PopupWarningMessage(NetworkMessage):
    lockDuration:int
    author:str
    content:str
    
    
    def __post_init__(self):
        super().__init__()
    