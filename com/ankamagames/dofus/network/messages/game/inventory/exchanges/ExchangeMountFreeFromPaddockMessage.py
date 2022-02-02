from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeMountFreeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    liberator:str
    
    
    def __post_init__(self):
        super().__init__()
    