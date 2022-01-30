from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    protocolId = 3831
    latency:int
    sampleCount:int
    max:int
    
    
