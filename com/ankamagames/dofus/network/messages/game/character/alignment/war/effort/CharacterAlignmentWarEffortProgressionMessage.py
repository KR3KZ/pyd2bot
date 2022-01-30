from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(INetworkMessage):
    protocolId = 7324
    alignmentWarEffortDailyLimit:int
    alignmentWarEffortDailyDonation:int
    alignmentWarEffortPersonalDonation:int
    
    
