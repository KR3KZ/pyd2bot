from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AlignmentWarEffortDonationResultMessage(INetworkMessage):
    protocolId = 6010
    result:int
    
    
