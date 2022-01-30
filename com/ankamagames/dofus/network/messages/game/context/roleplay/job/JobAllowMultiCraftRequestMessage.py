from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobAllowMultiCraftRequestMessage(NetworkMessage):
    protocolId = 5111
    enabled:bool
    
