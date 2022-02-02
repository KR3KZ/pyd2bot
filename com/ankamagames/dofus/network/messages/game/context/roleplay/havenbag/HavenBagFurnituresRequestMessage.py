from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HavenBagFurnituresRequestMessage(NetworkMessage):
    cellIds:list[int]
    funitureIds:list[int]
    orientations:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    