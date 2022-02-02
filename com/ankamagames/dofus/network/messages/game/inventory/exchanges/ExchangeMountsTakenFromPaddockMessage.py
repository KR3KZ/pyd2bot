from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeMountsTakenFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    ownername:str
    
    
    def __post_init__(self):
        super().__init__()
    