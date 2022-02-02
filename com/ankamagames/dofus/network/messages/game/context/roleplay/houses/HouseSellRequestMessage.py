from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HouseSellRequestMessage(NetworkMessage):
    instanceId:int
    amount:int
    forSale:bool
    
    
    def __post_init__(self):
        super().__init__()
    