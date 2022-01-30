from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(NetworkMessage):
    protocolId = 7324
    alignmentWarEffortDailyLimit:int
    alignmentWarEffortDailyDonation:int
    alignmentWarEffortPersonalDonation:int
    
