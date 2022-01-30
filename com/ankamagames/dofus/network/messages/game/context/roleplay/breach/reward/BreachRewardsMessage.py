from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


class BreachRewardsMessage(NetworkMessage):
    protocolId = 3565
    rewards:list[BreachReward]
    
