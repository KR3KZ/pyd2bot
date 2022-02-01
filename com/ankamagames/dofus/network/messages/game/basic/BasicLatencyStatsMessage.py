from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicLatencyStatsMessage(INetworkMessage):
    protocolId = 3831
    latency:int
    sampleCount:int
    max:int
    
    
