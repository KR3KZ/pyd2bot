from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SubscriptionZoneMessage(INetworkMessage):
    protocolId = 3082
    active:bool
    
    
