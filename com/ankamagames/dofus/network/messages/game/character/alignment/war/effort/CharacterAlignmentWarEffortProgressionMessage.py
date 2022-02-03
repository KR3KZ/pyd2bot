from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(NetworkMessage):
    alignmentWarEffortDailyLimit:int
    alignmentWarEffortDailyDonation:int
    alignmentWarEffortPersonalDonation:int
    

    def init(self, alignmentWarEffortDailyLimit:int, alignmentWarEffortDailyDonation:int, alignmentWarEffortPersonalDonation:int):
        self.alignmentWarEffortDailyLimit = alignmentWarEffortDailyLimit
        self.alignmentWarEffortDailyDonation = alignmentWarEffortDailyDonation
        self.alignmentWarEffortPersonalDonation = alignmentWarEffortPersonalDonation
        
        super().__init__()
    
    