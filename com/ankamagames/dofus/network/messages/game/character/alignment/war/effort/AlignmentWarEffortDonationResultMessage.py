from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonationResultMessage(NetworkMessage):
    protocolId = 6010
    result:int
    
    
