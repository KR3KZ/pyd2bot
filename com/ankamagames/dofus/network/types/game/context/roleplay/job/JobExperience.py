from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class JobExperience(NetworkMessage):
    jobId:int
    jobLevel:int
    jobXP:int
    jobXpLevelFloor:int
    jobXpNextLevelFloor:int
    
    
    def __post_init__(self):
        super().__init__()
    