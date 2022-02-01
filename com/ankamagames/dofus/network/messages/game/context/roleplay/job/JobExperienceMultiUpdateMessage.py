from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


class JobExperienceMultiUpdateMessage(NetworkMessage):
    experiencesUpdate:list[JobExperience]
    
    
