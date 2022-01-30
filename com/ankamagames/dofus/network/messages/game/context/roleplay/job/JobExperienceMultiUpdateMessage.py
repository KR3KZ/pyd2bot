from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


class JobExperienceMultiUpdateMessage(NetworkMessage):
    protocolId = 4771
    experiencesUpdate:JobExperience
    
    
