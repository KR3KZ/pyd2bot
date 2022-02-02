from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SimpleCharacterCharacteristicForPreset(NetworkMessage):
    keyword:str
    base:int
    additionnal:int
    
    
    def __post_init__(self):
        super().__init__()
    