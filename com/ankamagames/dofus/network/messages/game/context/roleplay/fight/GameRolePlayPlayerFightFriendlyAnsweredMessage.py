from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    
    
    def __post_init__(self):
        super().__init__()
    