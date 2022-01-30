from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(NetworkMessage):
    protocolId = 7324
    alignmentWarEffortDailyLimit:float
    alignmentWarEffortDailyDonation:float
    alignmentWarEffortPersonalDonation:float
    
