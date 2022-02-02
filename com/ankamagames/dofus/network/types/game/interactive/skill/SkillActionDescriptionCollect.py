from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescriptionTimed import SkillActionDescriptionTimed


@dataclass
class SkillActionDescriptionCollect(SkillActionDescriptionTimed):
    min:int
    max:int
    
    
    def __post_init__(self):
        super().__init__()
    