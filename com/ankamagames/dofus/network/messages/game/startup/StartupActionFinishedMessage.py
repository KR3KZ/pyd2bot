from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class StartupActionFinishedMessage(NetworkMessage):
    actionId:int
    success:bool
    automaticAction:bool
    
    
    def __post_init__(self):
        super().__init__()
    