from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AccountLoggingKickedMessage(NetworkMessage):
    days:int
    hours:int
    minutes:int
    
    
    def __post_init__(self):
        super().__init__()
    