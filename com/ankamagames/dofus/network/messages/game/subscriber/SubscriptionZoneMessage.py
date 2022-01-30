from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SubscriptionZoneMessage(NetworkMessage):
    protocolId = 3082
    active:bool
    
    
