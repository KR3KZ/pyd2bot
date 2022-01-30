from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward


class BreachRewardsMessage(INetworkMessage):
    protocolId = 3565
    rewards:BreachReward
    
    
