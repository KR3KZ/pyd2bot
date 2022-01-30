from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuestLimitationMessage(NetworkMessage):
    protocolId = 1036
    reason:int
    
