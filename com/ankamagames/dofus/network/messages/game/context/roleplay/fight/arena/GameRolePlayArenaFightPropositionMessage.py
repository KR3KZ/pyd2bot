from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    fightId:int
    alliesId:list[int]
    duration:int
    
    
    def __post_init__(self):
        super().__init__()
    