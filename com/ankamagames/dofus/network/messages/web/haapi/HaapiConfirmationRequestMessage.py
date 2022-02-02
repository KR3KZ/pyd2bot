from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HaapiConfirmationRequestMessage(NetworkMessage):
    kamas:int
    ogrines:int
    rate:int
    action:int
    
    
    def __post_init__(self):
        super().__init__()
    