from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SubscriptionLimitationMessage(INetworkMessage):
    protocolId = 969
    reason:int
    
    
