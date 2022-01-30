from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


class JobLevelUpMessage(NetworkMessage):
    protocolId = 8401
    newLevel:int
    jobsDescription:JobDescription
    
    
