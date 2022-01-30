from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience


class JobExperienceMultiUpdateMessage(INetworkMessage):
    protocolId = 4771
    experiencesUpdate:JobExperience
    
    
