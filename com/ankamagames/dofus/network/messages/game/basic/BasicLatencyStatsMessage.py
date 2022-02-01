from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    latency:int
    sampleCount:int
    max:int
    
    
