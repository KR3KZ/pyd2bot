from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SubscriptionLimitationMessage(NetworkMessage):
    protocolId = 969
    reason:int
    
    
