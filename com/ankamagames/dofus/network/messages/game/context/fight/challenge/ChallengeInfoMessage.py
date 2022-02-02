from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ChallengeInfoMessage(NetworkMessage):
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    
    
    def __post_init__(self):
        super().__init__()
    