from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class CharacterCreationRequestMessage(NetworkMessage):
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    
    
    def __post_init__(self):
        super().__init__()
    