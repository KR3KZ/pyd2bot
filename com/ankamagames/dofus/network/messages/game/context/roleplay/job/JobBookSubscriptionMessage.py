from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription


@dataclass
class JobBookSubscriptionMessage(NetworkMessage):
    subscriptions:list[JobBookSubscription]
    
    
    def __post_init__(self):
        super().__init__()
    