from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    fightId:int
    playerId:int
    accepted:bool
    
    
    def __post_init__(self):
        super().__init__()
    