from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    uid:int
    bought:bool
    
    
    def __post_init__(self):
        super().__init__()
    