from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightOptionStateUpdateMessage(NetworkMessage):
    fightId:int
    teamId:int
    option:int
    state:bool
    
    
    def __post_init__(self):
        super().__init__()
    