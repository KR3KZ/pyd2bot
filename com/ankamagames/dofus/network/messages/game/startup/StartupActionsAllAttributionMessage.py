from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class StartupActionsAllAttributionMessage(NetworkMessage):
    characterId:int
    
    
    def __post_init__(self):
        super().__init__()
    