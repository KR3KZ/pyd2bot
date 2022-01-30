from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


class JobDescriptionMessage(NetworkMessage):
    protocolId = 8838
    jobsDescription:list[JobDescription]
    
