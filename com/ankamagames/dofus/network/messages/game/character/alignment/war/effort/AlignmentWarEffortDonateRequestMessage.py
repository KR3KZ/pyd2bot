from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AlignmentWarEffortDonateRequestMessage(INetworkMessage):
    protocolId = 5249
    donation:int
    
    
