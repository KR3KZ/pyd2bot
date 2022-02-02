from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch


@dataclass
class ExtendedLockedBreachBranch(ExtendedBreachBranch):
    unlockPrice:int
    
    
    def __post_init__(self):
        super().__init__()
    