from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription


class JobBookSubscriptionMessage(INetworkMessage):
    protocolId = 8266
    subscriptions:JobBookSubscription
    
    
