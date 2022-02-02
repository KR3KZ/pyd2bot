from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class RemodelingInformation(NetworkMessage):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    