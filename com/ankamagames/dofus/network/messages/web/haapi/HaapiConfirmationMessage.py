from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class HaapiConfirmationMessage(NetworkMessage):
    kamas:int
    amount:int
    rate:int
    action:int
    transaction:str
    
    
    def __post_init__(self):
        super().__init__()
    