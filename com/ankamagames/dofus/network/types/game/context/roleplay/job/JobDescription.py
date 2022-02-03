from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription
    


class JobDescription(NetworkMessage):
    jobId:int
    skills:list['SkillActionDescription']
    

    def init(self, jobId:int, skills:list['SkillActionDescription']):
        self.jobId = jobId
        self.skills = skills
        
        super().__init__()
    
    