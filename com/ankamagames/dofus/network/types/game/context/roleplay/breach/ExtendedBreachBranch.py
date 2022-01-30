from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


class ExtendedBreachBranch(BreachBranch):
    protocolId = 9376
    rewards:list[BreachReward]
    modifier:int
    prize:int
    
