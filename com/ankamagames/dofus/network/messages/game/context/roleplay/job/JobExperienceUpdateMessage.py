from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


@dataclass
class JobExperienceUpdateMessage(NetworkMessage):
    experiencesUpdate:JobExperience
    
    
    def __post_init__(self):
        super().__init__()
    