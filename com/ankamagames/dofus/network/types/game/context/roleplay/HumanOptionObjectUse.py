from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


@dataclass
class HumanOptionObjectUse(HumanOption):
    delayTypeId:int
    delayEndTime:int
    objectGID:int
    
    
    def __post_init__(self):
        super().__init__()
    