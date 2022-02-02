from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HavenBagFurnitureInformation(NetworkMessage):
    cellId:int
    funitureId:int
    orientation:int
    
    
    def __post_init__(self):
        super().__init__()
    