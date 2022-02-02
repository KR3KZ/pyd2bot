from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TextInformationMessage(NetworkMessage):
    msgType:int
    msgId:int
    parameters:list[str]
    
    
    def __post_init__(self):
        super().__init__()
    