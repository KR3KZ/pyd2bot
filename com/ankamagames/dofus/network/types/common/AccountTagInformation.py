from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AccountTagInformation(NetworkMessage):
    nickname:str
    tagNumber:str
    
    
    def __post_init__(self):
        super().__init__()
    