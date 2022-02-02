from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    itemUID:int
    objectGID:int
    objectType:int
    
    
    def __post_init__(self):
        super().__init__()
    