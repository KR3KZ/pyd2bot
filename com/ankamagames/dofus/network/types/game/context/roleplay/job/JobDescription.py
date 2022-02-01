from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class JobDescription(NetworkMessage):
    jobId:int
    skills:list[SkillActionDescription]
    
    
