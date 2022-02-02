from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


@dataclass
class JobDescription(NetworkMessage):
    jobId:int
    skills:list[SkillActionDescription]
    
    
    def __post_init__(self):
        super().__init__()
    