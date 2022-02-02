from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch


@dataclass
class BreachBranchesMessage(NetworkMessage):
    branches:list[ExtendedBreachBranch]
    
    
    def __post_init__(self):
        super().__init__()
    