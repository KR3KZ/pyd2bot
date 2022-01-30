from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobAllowMultiCraftRequestMessage(INetworkMessage):
    protocolId = 5111
    enabled:bool
    
    
