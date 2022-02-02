from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


@dataclass
class ExtendedBreachBranch(BreachBranch):
    rewards:list[BreachReward]
    modifier:int
    prize:int
    
    
    def __post_init__(self):
        super().__init__()
    