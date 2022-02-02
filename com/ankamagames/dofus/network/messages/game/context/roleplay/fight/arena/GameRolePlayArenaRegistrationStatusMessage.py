from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    registered:bool
    step:int
    battleMode:int
    
    
    def __post_init__(self):
        super().__init__()
    