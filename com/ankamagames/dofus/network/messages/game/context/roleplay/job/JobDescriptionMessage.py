from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription


class JobDescriptionMessage(INetworkMessage):
    protocolId = 8838
    jobsDescription:JobDescription
    
    
