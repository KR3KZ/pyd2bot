from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SubscriptionZoneMessage(INetworkMessage):
    protocolId = 3082
    active:bool
    
    
