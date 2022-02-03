from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription
    


class JobDescriptionMessage(NetworkMessage):
    jobsDescription:list['JobDescription']
    

    def init(self, jobsDescription:list['JobDescription']):
        self.jobsDescription = jobsDescription
        
        super().__init__()
    
    