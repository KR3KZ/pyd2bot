from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription


class JobBookSubscriptionMessage(INetworkMessage):
    protocolId = 8266
    subscriptions:JobBookSubscription
    
    
