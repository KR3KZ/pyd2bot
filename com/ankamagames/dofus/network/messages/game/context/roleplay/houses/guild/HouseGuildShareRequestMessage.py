from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HouseGuildShareRequestMessage(NetworkMessage):
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    
    
    def __post_init__(self):
        super().__init__()
    