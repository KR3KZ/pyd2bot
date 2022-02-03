from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience
    


class JobExperienceUpdateMessage(NetworkMessage):
    experiencesUpdate:'JobExperience'
    

    def init(self, experiencesUpdate:'JobExperience'):
        self.experiencesUpdate = experiencesUpdate
        
        super().__init__()
    
    