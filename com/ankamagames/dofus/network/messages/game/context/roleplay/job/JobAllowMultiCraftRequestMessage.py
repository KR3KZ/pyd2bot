from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobAllowMultiCraftRequestMessage(INetworkMessage):
    protocolId = 5111
    enabled:bool
    
    
