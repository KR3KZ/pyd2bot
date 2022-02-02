from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceUpdateMessage import JobExperienceUpdateMessage


@dataclass
class JobExperienceOtherPlayerUpdateMessage(JobExperienceUpdateMessage):
    playerId:int
    
    
    def __post_init__(self):
        super().__init__()
    