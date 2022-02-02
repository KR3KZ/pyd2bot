from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HouseBuyResultMessage(NetworkMessage):
    houseId:int
    instanceId:int
    realPrice:int
    secondHand:bool
    bought:bool
    
    
    def __post_init__(self):
        super().__init__()
    