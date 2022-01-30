from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


class JobExperienceUpdateMessage(INetworkMessage):
    protocolId = 3940
    experiencesUpdate:JobExperience
    
    
