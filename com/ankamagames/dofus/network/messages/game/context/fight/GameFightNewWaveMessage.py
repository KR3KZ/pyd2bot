from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightNewWaveMessage(NetworkMessage):
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    
    
    def __post_init__(self):
        super().__init__()
    