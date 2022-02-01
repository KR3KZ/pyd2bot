from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


class JobDescriptionMessage(NetworkMessage):
    jobsDescription:list[JobDescription]
    
    
