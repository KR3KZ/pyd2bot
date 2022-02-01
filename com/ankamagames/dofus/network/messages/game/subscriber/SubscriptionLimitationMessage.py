from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SubscriptionLimitationMessage(INetworkMessage):
    protocolId = 969
    reason:int
    
    
