from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


class JobLevelUpMessage(INetworkMessage):
    protocolId = 8401
    newLevel:int
    jobsDescription:JobDescription
    
    
