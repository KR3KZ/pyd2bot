from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


@dataclass
class JobLevelUpMessage(NetworkMessage):
    newLevel:int
    jobsDescription:JobDescription
    
    
    def __post_init__(self):
        super().__init__()
    