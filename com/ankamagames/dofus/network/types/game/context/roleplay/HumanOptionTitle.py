from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


@dataclass
class HumanOptionTitle(HumanOption):
    titleId:int
    titleParam:str
    
    
    def __post_init__(self):
        super().__init__()
    