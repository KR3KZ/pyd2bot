from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AlignmentWarEffortDonateRequestMessage(INetworkMessage):
    protocolId = 5249
    donation:int
    
    
