from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ChallengeFightJoinRefusedMessage(NetworkMessage):
    playerId:int
    reason:int
    
    
    def __post_init__(self):
        super().__init__()
    