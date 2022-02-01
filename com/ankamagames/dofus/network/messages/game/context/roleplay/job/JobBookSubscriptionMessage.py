from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription


class JobBookSubscriptionMessage(NetworkMessage):
    subscriptions:list[JobBookSubscription]
    
    
