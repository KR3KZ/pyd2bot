from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdentificationFailedMessage(NetworkMessage):
    protocolId = 7135
    reason:int
    
    
