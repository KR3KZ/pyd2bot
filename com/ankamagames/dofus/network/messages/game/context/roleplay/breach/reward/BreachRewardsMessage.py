from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


@dataclass
class BreachRewardsMessage(NetworkMessage):
    rewards:list[BreachReward]
    
    
    def __post_init__(self):
        super().__init__()
    