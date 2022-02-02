from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HouseInformations(NetworkMessage):
    houseId:int
    modelId:int
    
    
    def __post_init__(self):
        super().__init__()
    