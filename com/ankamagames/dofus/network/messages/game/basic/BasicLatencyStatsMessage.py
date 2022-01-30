from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicLatencyStatsMessage(INetworkMessage):
    protocolId = 3831
    latency:int
    sampleCount:int
    max:int
    
    
