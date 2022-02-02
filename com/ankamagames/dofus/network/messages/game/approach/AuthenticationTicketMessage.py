from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AuthenticationTicketMessage(NetworkMessage):
    lang:str
    ticket:str
    
    
    def __post_init__(self):
        super().__init__()
    