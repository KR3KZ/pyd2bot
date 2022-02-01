from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


class BreachRewardsMessage(NetworkMessage):
    rewards:list[BreachReward]
    
    
