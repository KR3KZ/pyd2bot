from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription


class JobBookSubscriptionMessage(NetworkMessage):
    protocolId = 8266
    subscriptions:list[JobBookSubscription]
    
