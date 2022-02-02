from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


@dataclass
class InteractiveElementNamedSkill(InteractiveElementSkill):
    nameId:int
    
    
    def __post_init__(self):
        super().__init__()
    