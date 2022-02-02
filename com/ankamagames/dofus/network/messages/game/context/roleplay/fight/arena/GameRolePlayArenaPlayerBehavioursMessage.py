from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaPlayerBehavioursMessage(NetworkMessage):
    flags:list[str]
    sanctions:list[str]
    banDuration:int
    
    
    def __post_init__(self):
        super().__init__()
    