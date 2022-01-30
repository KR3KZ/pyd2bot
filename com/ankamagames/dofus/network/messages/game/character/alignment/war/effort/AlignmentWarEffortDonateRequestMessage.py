from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonateRequestMessage(NetworkMessage):
    protocolId = 5249
    donation:int
    
