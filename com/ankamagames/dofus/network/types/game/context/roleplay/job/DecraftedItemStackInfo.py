from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class DecraftedItemStackInfo(NetworkMessage):
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:list[int]
    runesQty:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    