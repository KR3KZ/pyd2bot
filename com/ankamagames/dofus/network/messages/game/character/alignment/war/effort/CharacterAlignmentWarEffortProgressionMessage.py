from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(INetworkMessage):
    protocolId = 7324
    alignmentWarEffortDailyLimit:int
    alignmentWarEffortDailyDonation:int
    alignmentWarEffortPersonalDonation:int
    
    
