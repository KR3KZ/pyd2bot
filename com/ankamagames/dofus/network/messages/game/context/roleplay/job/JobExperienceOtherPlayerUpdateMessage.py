from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceUpdateMessage import JobExperienceUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience
    


class JobExperienceOtherPlayerUpdateMessage(JobExperienceUpdateMessage):
    playerId:int
    

    def init(self, playerId:int, experiencesUpdate:'JobExperience'):
        self.playerId = playerId
        
        super().__init__(experiencesUpdate)
    
    