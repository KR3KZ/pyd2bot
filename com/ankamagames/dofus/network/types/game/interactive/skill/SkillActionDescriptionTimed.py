from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


@dataclass
class SkillActionDescriptionTimed(SkillActionDescription):
    time:int
    
    
    def __post_init__(self):
        super().__init__()
    