from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


class JobExperienceUpdateMessage(NetworkMessage):
    protocolId = 3940
    experiencesUpdate:JobExperience
    
    
