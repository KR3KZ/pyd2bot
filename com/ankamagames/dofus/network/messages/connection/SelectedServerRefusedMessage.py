from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SelectedServerRefusedMessage(NetworkMessage):
    serverId:int
    error:int
    serverStatus:int
    
    
    def __post_init__(self):
        super().__init__()
    